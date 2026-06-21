class ListUtils:
    @staticmethod
    def find_common_elements(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        intersection = set1.intersection(set2)
        return sorted(intersection)

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 7, 1]
    sample_list2 = [8, 6, 4, 2, 0, 9, 7]
    print(ListUtils.find_common_elements(sample_list1, sample_list2))