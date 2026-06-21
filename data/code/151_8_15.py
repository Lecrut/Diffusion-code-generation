def merge_and_sort_floats(list1, list2):
    combined_set = set(list1).union(set(list2))
    return sorted(combined_set)

if __name__ == '__main__':
    float_list1 = [3.5, 1.2, 4.8]
    float_list2 = [2.9, 1.2, 6.0]
    result = merge_and_sort_floats(float_list1, float_list2)
    print(result)