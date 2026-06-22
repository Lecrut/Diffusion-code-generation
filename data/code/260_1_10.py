class ListComparator:
    @staticmethod
    def find_common_elements(list1, list2):
        return [element for element in list1 if element in list2]

if __name__ == '__main__':
    sample_list1 = [1, 5, 3, 7]
    sample_list2 = [2, 4, 6, 1]
    common_elements = ListComparator.find_common_elements(sample_list1, sample_list2)
    print(common_elements)