class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare(self):
        return [f"{x} > {y}" if x > y else f"{x} < {y}" if x < y else f"{x} == {y}" for x, y in zip(self.list1, self.list2)]

if __name__ == '__main__':
    comparator = ListComparator([1, 5, 10, 15], [2, 4, 10, 20])
    results = comparator.compare()
    for result in results:
        print(result)