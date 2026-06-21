def locate_longest_string(input_list):
    if not hasattr(input_list, '__iter__'):
        raise ValueError('Input must be an iterable')
    longest_str = None
    max_length = 0
    for item in input_list:
        if isinstance(item, str) and len(item) > max_length:
            longest_str = item
            max_length = len(item)
    return longest_str
if __name__ == '__main__':
    sample_input_1 = ['apple', 'banana', 'cherry', 123, None]
    try:
        result_1 = locate_longest_string(sample_input_1)
        print(result_1)
    except ValueError as e:
        print(e)
    sample_input_2 = ['short', 'longer string', 'longest_string_is_here']
    try:
        result_2 = locate_longest_string(sample_input_2)
        print(result_2)
    except ValueError as e:
        print(e)
    sample_input_3 = [None, None, None]
    try:
        result_3 = locate_longest_string(sample_input_3)
        print(result_3)
    except ValueError as e:
        print(e)
    sample_input_4 = []
    try:
        result_4 = locate_longest_string(sample_input_4)
        print(result_4)
    except ValueError as e:
        print(e)