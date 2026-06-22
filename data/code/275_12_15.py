def is_list(item):
    return isinstance(item, list)

def flatten_and_print(nested_list):
    if not is_list(nested_list):
        raise ValueError("Input must be a list")
    
    for item in nested_list:
        if is_list(item):
            flatten_and_print(item)
        else:
            print(item)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    flatten_and_print(sample_data)