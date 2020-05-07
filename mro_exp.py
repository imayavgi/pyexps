import pprint
class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]
    
    def sort(self):
        self._items.sort()
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "SimpleList({!r})".format(self._items)

class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()
    
    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))

class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("integer values only allowed in IntList")
    
    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "InstList({!r})".format(list(self))

class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedInstList({!r})".format(list(self))


if __name__ == "__main__":
    # run this using python -m trace --trace mro_exp.py
    pp = pprint.PrettyPrinter()
    pp.pprint(SortedIntList.mro())
    pp.pprint(IntList.mro())
    il = IntList([4,5,7,8])
    pp.pprint(il)
    pp.pprint(super(IntList, il))
    sil = SortedIntList([13, 5, 9, 4, 8])
    pp.pprint(sil)
    sil.add(19)
    pp.pprint(sil)
    pp.pprint(super(SortedIntList, sil))