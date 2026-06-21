class ListComparator:
    @staticmethod
    def are_sets_equal(set_a, set_b):
        return set_a == set_b

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 5, 4]
    list3 = [1, 2, 3, 4]
    
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    result1 = ListComparator.are_sets_equal(set1, set2)
    print(f"Comparing {list1} and {list2}: Equality={result1}")
    
    result2 = ListComparator.are_sets_equal(set1, set3)
    print(f"Comparing {list1} and {list3}: Equality={result2}")