def print_element_at_index(data_list, index):

    def is_valid_index(lst, idx):
        return 0 <= idx < len(lst)
    if not isinstance(data_list, list):
        raise TypeError('The first argument must be a list.')
    if not isinstance(index, int):
        raise TypeError('The second argument must be an integer.')
    if not is_valid_index(data_list, index):
        raise IndexError('Index is out of the bounds of the list.')
    print(data_list[index])
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print_element_at_index(sample_list, 2)
        print_element_at_index(sample_list, -1)
    except Exception as e:
        print(e)