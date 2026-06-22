def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        raise ValueError('Index out of range')
    except TypeError:
        raise ValueError('Invalid sequence type')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd', 'e')
    print(get_element(sample_list, 2))
    print(get_element(sample_tuple, 3))
    try:
        print(get_element(sample_list, 10))
    except ValueError as e:
        print(e)
    try:
        print(get_element(12345, 0))
    except ValueError as e:
        print(e)