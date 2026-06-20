class ListComparator:
    def compare(self, list1, list2):
        return [f"{x} > {y}" if x > y else f"{x} < {y}" if x < y else f"{x} == {y}" for x, y in zip(list1, list2)]

if __name__ == '__main__':
    comparator = ListComparator()
    result1 = comparator.compare([1, 5, 10, 15], [2, 4, 10, 20])
    print(result1)
    result2 = comparator.compare([3, 7, 12, 18], [2, 8, 10, 25])
    print(result2)