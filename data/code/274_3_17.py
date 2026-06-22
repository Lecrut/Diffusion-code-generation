def flatten_and_print(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            flatten_and_print(item)
        else:
            print(item)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 'a', ['b', 'c'], [], {}, {'key': 'value'}]
    flatten_and_print(sample_data)