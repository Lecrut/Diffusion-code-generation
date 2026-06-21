from itertools import chain

class TupleComparer:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare(self):
        return set(chain.from_iterable(self.list1)) == set(chain.from_iterable(self.list2))

if __name__ == '__main__':
    comparer = TupleComparer([(1, 2), (3, 4)], [(4, 3), (2, 1)])
    print(comparer.compare())