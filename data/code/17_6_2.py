def get_last_element(data):
    if not isinstance(data, list):
        raise TypeError('Input must be a list')
    if not data:
        raise ValueError('List is empty')
    return data[-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)