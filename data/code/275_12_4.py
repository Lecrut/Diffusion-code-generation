def flatten_and_print(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            flatten_and_print(element)
        else:
            print(element)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    flatten_and_print(sample_data)