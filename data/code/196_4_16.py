class ListCombiner:
    def __init__(self):
        self.list1 = [1, 2, 3]
        self.list2 = ['a', 'b', 'c']

    def combine_lists(self):
        return self.list1 + self.list2

if __name__ == '__main__':
    combiner = ListCombiner()
    result = combiner.combine_lists()
    print(result)