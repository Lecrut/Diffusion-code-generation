def get_value_with_fallback(data, key, default):
    try:
        return data[key]
    except KeyError:
        return default

if __name__ == '__main__':
    sample_dict = {'name': 'Alice', 'age': 30}
    result1 = get_value_with_fallback(sample_dict, 'name', 'Unknown')
    result2 = get_value_with_fallback(sample_dict, 'city', 'Unknown')
    print(result1)
    print(result2)