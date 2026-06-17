def memory_efficient_iterator(data):
    for key in data:
        yield (key, data[key])
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20, 'c': 30}
    result_dict = {}
    iterator = memory_efficient_iterator(sample_data)
    for key_value in iterator:
        k, v = key_value
        result_dict[k] = v
    print(result_dict)