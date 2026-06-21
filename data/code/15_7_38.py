class ListComparator:
    @staticmethod
    def compare_lists(list1, list2):
        if len(list1) != len(list2):
            return False
        for elem1, elem2 in zip(list1, list2):
            if elem1 != elem2:
                return False
        return True

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 4, 5]
    sample_list3 = [1, 2, 3, 4, 6]
    print(ListComparator.compare_lists(sample_list1, sample_list2))
    print(ListComparator.compare_lists(sample_list1, sample_list3))