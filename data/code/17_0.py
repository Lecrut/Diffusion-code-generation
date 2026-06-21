def get_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    if len(lst) == 0:
        raise ValueError('List must not be empty')
    return lst[-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)
    another_sample = ['apple', 'banana', 'cherry']
    result2 = get_last_element(another_sample)
    print(result2)
    mixed_sample = [1, 'two', 3.0, {'key': 'value'}]
    result3 = get_last_element(mixed_sample)
    print(result3)