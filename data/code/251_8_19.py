def determine_the_largest_number_present_compare(list1, list2):
    max_list1 = max(list1) if list1 else None
    max_list2 = max(list2) if list2 else None
    result = {}
    result['list1_max'] = max_list1
    result['list2_max'] = max_list2
    if max_list1 is not None and max_list2 is not None:
        result['largest_number'] = max(max_list1, max_list2)
    elif max_list1 is not None:
        result['largest_number'] = max_list1
    elif max_list2 is not None:
        result['largest_number'] = max_list2
    else:
        result['largest_number'] = None
    return result

if __name__ == '__main__':
    sample_list_1 = [3.14, 1.618, 2.718, 0.577]
    sample_list_2 = [-10.5, -5.2, -20.1, -1.0]
    result = determine_the_largest_number_present_compare(sample_list_1, sample_list_2)
    print(result)