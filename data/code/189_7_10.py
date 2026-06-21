def remove_element_from_path(nested_list, path):
    if not isinstance(path, list) or not all((isinstance(i, int) for i in path)):
        raise ValueError('Path must be a list of integers.')
    current = nested_list
    for index in path[:-1]:
        if not isinstance(current[index], list):
            raise IndexError('Invalid path. Non-list element encountered.')
        current = current[index]
    if path[-1] >= len(current):
        raise IndexError('Index out of range.')
    del current[path[-1]]
if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]]]
    remove_element_from_path(sample_list, [1, 1])
    print(sample_list)
    sample_list_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    remove_element_from_path(sample_list_2, [2, 1])
    print(sample_list_2)
    sample_list_3 = [[[1, 2], 3], 4]
    remove_element_from_path(sample_list_3, [0, 0, 1])
    print(sample_list_3)