class ListCombiner:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def concatenate(self):
        return self.list1 + self.list2

if __name__ == '__main__':
    combiner = ListCombiner([1, 2], ['a', 'b'])
    print(combiner.concatenate())