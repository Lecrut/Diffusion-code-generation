def print_first_value(d):
    items = list(d.items())
    if not items:
        return
    return items[0][1]

if __name__ == '__main__':
    sample_dict = {"key1": 10, "key2": 20, "key3": 30}
    result = print_first_value(sample_dict)
    print(result)