def combine_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both arguments must be lists")
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    try:
        sample_list1 = [1, 2, 3]
        sample_list2 = [4, 5, 6]
        combined_list = combine_lists(sample_list1, sample_list2)
        print(combined_list)
    except ValueError as e:
        print(e)