def merge_and_sort_floats(list1, list2):
    combined = list1 + list2
    unique_elements = set(combined)
    sorted_list = sorted(unique_elements)
    return sorted_list

if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 4.8]
    sample_list2 = [2.9, 1.2, 6.0]
    result = merge_and_sort_floats(sample_list1, sample_list2)
    print(result)