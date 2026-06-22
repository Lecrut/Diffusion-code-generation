def get_first_value(data):
    keys = list(data.keys())
    return data[keys[0]]

if __name__ == '__main__':
    sample_dict = {
        "alpha": 1,
        "beta": 2,
        "gamma": 3
    }
    result = get_first_value(sample_dict)
    print(result)