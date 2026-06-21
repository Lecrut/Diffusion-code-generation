def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        raise ValueError('Index out of range')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300, 400, 500)
    print(get_element(sample_list, 2))
    print(get_element(sample_tuple, 3))
    try:
        print(get_element(sample_list, 10))
    except ValueError as e:
        print(e)