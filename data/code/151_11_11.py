def merge_lists(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists")
    result_list = list_a[:]
    result_list.extend(list_b)
    return result_list

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    try:
        merged_list = merge_lists(sample_list1, sample_list2)
        print("Merged List:", merged_list)
    except ValueError as e:
        print(e)