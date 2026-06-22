class ListComparator:
    def find_common_elements(self, list1, list2):
        return [element for element in list1 if element in list2]

if __name__ == '__main__':
    comparator = ListComparator()
    print(comparator.find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    print(comparator.find_common_elements(['apple', 'banana'], ['banana', 'cherry']))