def get_last_item(data):
    if not data:
        return None
    keys = list(data.keys())
    last_key = keys[-1]
    return (last_key, data[last_key])

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    result = get_last_item(sample_dict)
    print(result)