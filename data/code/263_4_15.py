class CommonElements:
    @staticmethod
    def find_common_elements(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return list(set1.intersection(set2))

if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2, 8]
    sample_list_2 = [5, 7, 1, 9, 0]
    common_elements = CommonElements.find_common_elements(sample_list_1, sample_list_2)
    print(f"Common elements: {common_elements}")