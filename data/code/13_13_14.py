def get_value_with_fallback(data, key, default):
    try:
        return data[key]
    except KeyError:
        return default

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20}
    result1 = get_value_with_fallback(sample_dict, 'a', 0)
    result2 = get_value_with_fallback(sample_dict, 'c', 999)
    print(result1)
    print(result2)