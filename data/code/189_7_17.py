def remove_from_nested_list(nested_list, path):
    current = nested_list
    for key in path[:-1]:
        if isinstance(current[key], list):
            current = current[key]
        else:
            raise ValueError('Invalid path')
    del current[path[-1]]
if __name__ == '__main__':
    sample_list = [[1, 2, 3], [4, [5, 6]], [7, 8, 9]]
    path_to_remove = [1, 1, 0]
    remove_from_nested_list(sample_list, path_to_remove)
    print(sample_list)