def find_intersection(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return list(set_a & set_b)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 2, 5]
    list2 = [4, 5, 6, 2, 1]
    result = find_intersection(list1, list2)
    print(result)