def memory_efficient_iterator(data):
    for key in data:
        yield (key, data[key])
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20, 'c': 30}
    result_dict = {}
    for key, value in memory_efficient_iterator(sample_data):
        result_dict[key] = value
    print(result_dict)