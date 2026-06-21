def remove_item(nested_list, path):
    current = nested_list
    for key in path[:-1]:
        if isinstance(current[key], list):
            current = current[key]
        else:
            raise ValueError(f"Invalid path: {path}")
    del current[path[-1]]

if __name__ == '__main__':
    sample_list = [
        ['a', 'b'],
        ['c', ['d', 'e']],
        ['f', ['g', ['h', 'i']]]
    ]
    remove_item(sample_list, [2, 1, 0])
    print(sample_list)