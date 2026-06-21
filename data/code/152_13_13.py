class ListUtils:
    @staticmethod
    def get_intersection(list1, list2):
        if not all(isinstance(item, (list, frozenset)) for item in [list1, list2]):
            raise ValueError("Both inputs must be lists or frozensets.")
        
        set1 = set(frozenset(list1))
        set2 = set(frozenset(list2))
        
        return list(set1 & set2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = ListUtils.get_intersection(list_a, list_b)
    print(f"Intersection of {list_a} and {list_b}: {result1}")
    
    frozenset_c = frozenset([10, 20, 30])
    frozenset_d = frozenset([30, 40, 50])
    result2 = ListUtils.get_intersection(frozenset_c, frozenset_d)
    print(f"Intersection of {frozenset_c} and {frozenset_d}: {result2}")