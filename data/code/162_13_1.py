def filter_dict(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[key] = value
    return new_dict
if __name__ == '__main__':
    sample_dict = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    result = filter_dict(sample_dict)
    print(result)