def flatten_and_print(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            flatten_and_print(item)
        else:
            print(item)

if __name__ == '__main__':
    sample_data = [1, ['a', 'b'], ['c', ['d', 'e']], 'f']
    flatten_and_print(sample_data)