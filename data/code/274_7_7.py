class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_common_elements(self):
        return [element for element in self.list1 if element in self.list2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    comparator = ListComparator(sample_list1, sample_list2)
    common_elements = comparator.find_common_elements()
    print(common_elements)