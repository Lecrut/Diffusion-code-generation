def get_value(d, key, default=None):
    return d.get(key, default)

if __name__ == '__main__':
    sample_dict = {"name": "Alice", "age": 30}
    print(get_value(sample_dict, "name"))
    print(get_value(sample_dict, "city", "Unknown"))