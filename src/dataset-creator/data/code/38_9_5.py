def memory_efficient_iterator(data):
    for key in data:
        yield (key, data[key])
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20, 'c': 30}
    it = memory_efficient_iterator(sample_data)
    result_dict = {}
    for key, value in it:
        result_dict[key] = value
    print(result_dict)