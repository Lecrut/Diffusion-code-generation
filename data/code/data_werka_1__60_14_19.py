def fetch_last_item(array):
    if not isinstance(array, (list, tuple)):
        raise TypeError('Input must be a list or tuple')
    if len(array) == 0:
        raise ValueError('Array cannot be empty')
    return array[-1]
if __name__ == '__main__':
    sample_array_1 = [1, 2, 3, 4, 5]
    print(fetch_last_item(sample_array_1))
    sample_tuple_1 = (10, 20, 30)
    print(fetch_last_item(sample_tuple_1))
    try:
        empty_list = []
        print(fetch_last_item(empty_list))
    except ValueError as e:
        print(e)
    try:
        invalid_input = 'not a list or tuple'
        print(fetch_last_item(invalid_input))
    except TypeError as e:
        print(e)