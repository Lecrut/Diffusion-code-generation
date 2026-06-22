class ListComparator:
    @staticmethod
    def find_common_elements(list1, list2):
        return [element for element in list1 if element in list2]

if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2, 8]
    sample_list_2 = [-10, 5, 0, -20, 3]
    common_elements = ListComparator.find_common_elements(sample_list_1, sample_list_2)
    print(f"Common elements: {common_elements}")