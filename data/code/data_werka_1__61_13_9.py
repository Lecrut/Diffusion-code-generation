def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        raise ValueError(f'Index {index} is out of range for the given sequence.')
    except TypeError:
        raise TypeError('The provided sequence must be an iterable.')
if __name__ == '__main__':
    sample_tuple = (100, 200, 300, 400, 500)
    sample_list = ['x', 'y', 'z', 'w', 'v']
    try:
        print(get_element(sample_tuple, 2))
    except Exception as e:
        print(e)
    try:
        print(get_element(sample_list, 4))
    except Exception as e:
        print(e)