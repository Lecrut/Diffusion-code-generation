def get_last_key_value_pair(d):
    if not d:
        raise ValueError("Dictionary is empty")
    last_key = list(d.keys())[-1]
    return (last_key, d[last_key])

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_last_key_value_pair(sample_dict)
    print(result)