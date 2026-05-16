def filter_dict(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[key] = value
    return new_dict
if __name__ == '__main__':
    sample_dict = {"a": 1, "b": 2, "c": 3}
    result = filter_dict(sample_dict)
    print(result)