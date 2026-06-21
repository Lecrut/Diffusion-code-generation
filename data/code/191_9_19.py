def validate_lists(list_one, list_two):
    if not isinstance(list_one, list) or not isinstance(list_two, list):
        raise ValueError("Both inputs must be lists")
    return True

def join_lists(list_one, list_two):
    validate_lists(list_one, list_two)
    combined_list = list_one + list_two
    return combined_list

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = join_lists(list_a, list_b)
    print(result)

    list_c = ['apple', 'banana', 'cherry']
    list_d = ['banana', 'date', 'elderberry']
    result2 = join_lists(list_c, list_d)
    print(result2)