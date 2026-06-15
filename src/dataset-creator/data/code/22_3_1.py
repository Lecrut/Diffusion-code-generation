def filter_and_merge(list_of_tuples, input_dict):
    result_dict = {}
    for key, value in list_of_tuples:
        if key in input_dict:
            result_dict[key] = value
    return result_dict
if __name__ == '__main__':
    sample_list = [('a', 10), ('b', 20), ('c', 30), ('d', 40)]
    sample_dict = {'a': 100, 'b': 200, 'e': 50}
    output = filter_and_merge(sample_list, sample_dict)
    print(output)