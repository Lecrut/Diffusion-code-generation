def join_lists(list1, list2):
    if not all(isinstance(item, list) for item in [list1, list2]):
        raise ValueError("Both arguments must be lists")
    return [*list1, *list2]

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [10, 11, 12]
    result = join_lists(sample_list1, sample_list2)
    print(result)