def get_element(sequence, index):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError('Invalid sequence type')
    if index < 0 or index >= len(sequence):
        raise ValueError('Index out of range')
    return sequence[index]

if __name__ == '__main__':
    sample_data = {
        'list': [10, 20, 30, 40, 50],
        'tuple': (100, 200, 300, 400, 500),
        'string': "hello"
    }
    
    try:
        print(get_element(sample_data['list'], 2))
    except ValueError as e:
        print(e)
    
    try:
        print(get_element(sample_data['tuple'], 3))
    except ValueError as e:
        print(e)
    
    try:
        print(get_element(sample_data['string'], 1))
    except ValueError as e:
        print(e)
    
    try:
        print(get_element(12345, 1))
    except ValueError as e:
        print(e)