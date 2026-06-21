def remove_element_at_path(nested_list, path):
    current = nested_list
    for i in range(len(path) - 1):
        if isinstance(current[path[i]], list):
            current = current[path[i]]
        else:
            raise ValueError('Path contains non-list element')
    if isinstance(current[path[-1]], list):
        del current[path[-1]][0]
    elif isinstance(current[path[-1]], int):
        del current[path[-1]]
    else:
        raise ValueError('Invalid path to remove an element')
if __name__ == '__main__':
    sample_list = [1, 2, [3, 4, [5, 6], 7], 8]
    path_to_remove = [2, 2, 0]
    remove_element_at_path(sample_list, path_to_remove)
    print(sample_list)