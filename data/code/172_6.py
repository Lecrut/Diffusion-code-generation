def get_keys(data):
    return list(data.keys())
if __name__ == '__main__':
    sample_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    keys_list = get_keys(sample_dict)
    print(keys_list)