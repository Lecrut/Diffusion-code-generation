def remove_nested_item(nested_list, path):
    current = nested_list
    for item in path[:-1]:
        current = current[item]
    del current[path[-1]]

if __name__ == '__main__':
    sample_list = [1, 2, [3, 4, [5, 6], 7], 8]
    path_to_remove = [2, 2, 0]
    remove_nested_item(sample_list, path_to_remove)
    print(sample_list)