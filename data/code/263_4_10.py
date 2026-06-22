class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_common_elements(self):
        return [element for element in self.list1 if element in self.list2]

if __name__ == '__main__':
    comparator = ListComparator([3, 1, 4, 1, 5, 9, 2, 8], [-10, 5, 0, -20, 3])
    common_elements = comparator.find_common_elements()
    print(f"Common elements: {common_elements}")