def get_last_item(d):
    if not d:
        return None
    keys = list(d.keys())
    last_key = keys[-1]
    return last_key, d[last_key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_last_item(sample_dict)
    print(result)