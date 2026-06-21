class CommonElementsFinder:
    @staticmethod
    def find_common_elements(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return set1.intersection(set2)

if __name__ == '__main__':
    finder = CommonElementsFinder()
    sample_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sample_list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    common_elements = finder.find_common_elements(sample_list1, sample_list2)
    print(common_elements)