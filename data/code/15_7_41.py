def are_lists_identical(list1, list2):
    try:
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise ValueError('Both inputs must be lists')
        if len(list1) != len(list2):
            return False
        for elem1, elem2 in zip(list1, list2):
            if elem1 != elem2:
                return False
        return True
    except Exception as e:
        print(f'An error occurred: {e}')
        return False
if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [10, 20, 30, 40, 50]
    list_c = [10, 20, 30, 40, 60]
    print(are_lists_identical(list_a, list_b))
    print(are_lists_identical(list_a, list_c))
    invalid_input_1 = 'not a list'
    invalid_input_2 = [1, 2, 3]
    print(are_lists_identical(invalid_input_1, invalid_input_2))