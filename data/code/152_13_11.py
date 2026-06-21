def get_intersection(list1, list2):
    if not all(isinstance(item, frozenset) for item in (list1, list2)):
        raise ValueError("Both inputs must be frozensets")
    
    return list(frozenset.bitwise_and(list1, list2))

if __name__ == '__main__':
    set_a = frozenset([1, 2, 3, 4, 5])
    set_b = frozenset([4, 5, 6, 7, 8])
    result1 = get_intersection(set_a, set_b)
    print(f"Intersection of {set_a} and {set_b}: {result1}")
    
    set_c = frozenset(['a', 'b', 'c', 'd'])
    set_d = frozenset(['c', 'd', 'e', 'f'])
    result2 = get_intersection(set_c, set_d)
    print(f"Intersection of {set_c} and {set_d}: {result2}")