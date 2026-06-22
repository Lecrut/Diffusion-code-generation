def is_list(element):
    return isinstance(element, list)

def flatten_and_print(nested_list):
    for item in nested_list:
        if is_list(item):
            flatten_and_print(item)
        else:
            print(item)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    flatten_and_print(sample_data)