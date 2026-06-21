def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        raise ValueError('Index out of range')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd', 'e')
    index_to_access = 2
    print(get_element(sample_list, index_to_access))
    print(get_element(sample_tuple, index_to_access))