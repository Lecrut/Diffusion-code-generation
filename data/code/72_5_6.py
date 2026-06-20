class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_pairs(self):
        for item1, item2 in zip(self.list1, self.list2):
            if item1 > item2:
                yield f'{item1} > {item2}'
            elif item1 < item2:
                yield f'{item1} < {item2}'
            else:
                yield f'{item1} == {item2}'

if __name__ == '__main__':
    comparator = ListComparator([3, 5, 7], [2, 4, 6])
    for comparison in comparator.compare_pairs():
        print(comparison)