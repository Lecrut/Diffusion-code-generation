def get_element(sequence, index):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError('Invalid sequence type')
    try:
        return sequence[index]
    except IndexError:
        raise ValueError('Index out of range')

if __name__ == '__main__':
    sample_data = {
        'list': [10, 20, 30, 40, 50],
        'tuple': (100, 200, 300, 400, 500),
        'string': 'hello'
    }
    
    print(get_element(sample_data['list'], 2))
    print(get_element(sample_data['tuple'], 3))
    try:
        print(get_element(sample_data['list'], 10))
    except ValueError as e:
        print(e)
    try:
        print(get_element(sample_data['string'], 2))
    except ValueError as e:
        print(e)
    try:
        print(get_element(12345, 1))
    except ValueError as e:
        print(e)