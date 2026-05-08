def find_intersection(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = set_a.intersection(set_b)
    return list(intersection)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    result1 = find_intersection(list1, list2)
    print(f"Intersection of {list1} and {list2}: {result1}")
    list3 = [10, 20, 30, 40]
    list4 = [30, 40, 50, 60]
    result2 = find_intersection(list3, list4)
    print(f"Intersection of {list3} and {list4}: {result2}")
    list5 = ['a', 'b', 'c', 'd']
    list6 = ['c', 'd', 'e', 'f']
    result3 = find_intersection(list5, list6)
    print(f"Intersection of {list5} and {list6}: {result3}")