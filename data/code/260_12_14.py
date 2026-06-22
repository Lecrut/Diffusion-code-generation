class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_unique_elements(self):
        unique_in_list1 = [element for element in self.list1 if element not in self.list2]
        unique_in_list2 = [element for element in self.list2 if element not in self.list1]
        return unique_in_list1, unique_in_list2

if __name__ == '__main__':
    comparator = ListComparator([1.1, 2.2, 3.3, 4.4], [3.3, 4.4, 5.5, 6.6])
    unique_elements = comparator.find_unique_elements()
    print("Unique elements in list1:", sorted(unique_elements[0]))
    print("Unique elements in list2:", sorted(unique_elements[1]))