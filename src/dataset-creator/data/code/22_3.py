def filter_and_merge(list_of_tuples, input_dict):
    result_dict = {}
    for key, value in list_of_tuples:
        if key in input_dict:
            result_dict[key] = value
    return result_dict
if __name__ == '__main__':
    data_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    source_dict = {'a': 100, 'b': 200, 'e': 500}
    output = filter_and_merge(data_list, source_dict)
    print(output)