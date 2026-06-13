def get_keys(data):
    return list(data.keys())
if __name__ == '__main__':
    sample_dict = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    keys_list = get_keys(sample_dict)
    print(keys_list)