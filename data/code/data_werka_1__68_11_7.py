def absolute_difference_generator(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    sample_values = {
        'data_set_1': [8, 16, 24, 32],
        'data_set_2': [2, 4, 6, 8]
    }
    try:
        for diff in absolute_difference_generator(sample_values['data_set_1'], sample_values['data_set_2']):
            print(diff)
    except ValueError as e:
        print(e)