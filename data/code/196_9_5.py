def validate_lists(list_x, list_y):
    if not isinstance(list_x, list) or not isinstance(list_y, list):
        raise ValueError("Both arguments must be lists")

def concatenate_lists(list_x, list_y):
    validate_lists(list_x, list_y)
    result = list_x[:]
    result[len(result):] = list_y
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    print(concatenate_lists(sample_list1, sample_list2))