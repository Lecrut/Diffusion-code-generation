def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5]
    sample_list_b = [4, 5, 6, 7, 8]
    intersection_result = find_intersection(sample_list_a, sample_list_b)
    print(intersection_result)

    sample_list_c = ['apple', 'banana', 'cherry']
    sample_list_d = ['banana', 'date', 'apple']
    intersection_result = find_intersection(sample_list_c, sample_list_d)
    print(intersection_result)