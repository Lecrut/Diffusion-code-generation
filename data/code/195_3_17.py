class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def count_common_elements(self):
        return len(set(self.list1) & set(self.list2))

if __name__ == '__main__':
    comparator = ListComparator(["apple", "banana", "cherry", "date"], ["apple", "orange", "cherry", "grape"])
    common_count = comparator.count_common_elements()
    print(common_count)