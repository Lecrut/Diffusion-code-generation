def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    sample_tuple = (10, 20, 30)
    index_to_access = 3
    element_from_list = get_element(sample_list, index_to_access)
    element_from_tuple = get_element(sample_tuple, index_to_access + 1)
    print(f'Element at index {index_to_access} in the list: {element_from_list}')
    print(f'Element at index {index_to_access + 1} in the tuple (out of bounds): {element_from_tuple}')