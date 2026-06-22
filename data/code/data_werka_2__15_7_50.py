class ListComparator:
    @staticmethod
    def are_identical(list1, list2):
        if len(list1) != len(list2):
            return False
        for elem1, elem2 in zip(list1, list2):
            if elem1 != elem2:
                return False
        return True

if __name__ == '__main__':
    sample_list1 = [100, 200, 300, 400, 500]
    sample_list2 = [100, 200, 300, 400, 500]
    sample_list3 = [100, 200, 300, 400, 600]
    
    comparator = ListComparator()
    print(comparator.are_identical(sample_list1, sample_list2))
    print(comparator.are_identical(sample_list1, sample_list3))