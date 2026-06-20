class ListComparator:
    def are_lists_identical(self, list1, list2):
        if len(list1) != len(list2):
            return False
        for item1, item2 in zip(list1, list2):
            if not (isinstance(item1, list) and isinstance(item2, list)) and item1 is not item2:
                return False
        return True

if __name__ == '__main__':
    comparator = ListComparator()
    
    sample_list1 = [1, 2, 3]
    sample_list2 = [1, 2, 3]
    print(comparator.are_lists_identical(sample_list1, sample_list2))
    
    sample_list3 = [1, 2, 4]
    print(comparator.are_lists_identical(sample_list1, sample_list3))
    
    sample_list4 = [[1], [2], [3]]
    sample_list5 = [[1], [2], [3]]
    print(comparator.are_lists_identical(sample_list4, sample_list5))
    
    sample_list6 = [[1], [2], [4]]
    print(comparator.are_lists_identical(sample_list4, sample_list6))