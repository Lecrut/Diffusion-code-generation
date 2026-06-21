def is_valid_list(input_list):
    return isinstance(input_list, list)

def merge_lists(list1, list2):
    if not is_valid_list(list1) or not is_valid_list(list2):
        raise ValueError("Both arguments must be lists")
    return [*list1, *list2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    try:
        merged_list = merge_lists(sample_list1, sample_list2)
        print(merged_list)
    except ValueError as e:
        print(e)