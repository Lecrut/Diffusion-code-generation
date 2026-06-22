class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_equal_indices(self):
        return [i for i, (a, b) in enumerate(zip(self.list1, self.list2)) if a == b]

if __name__ == '__main__':
    comparator = ListComparator([1.0, 2.5, 3.0, 4.5], [1.0, 2.6, 3.0, 4.5])
    print(comparator.find_equal_indices())