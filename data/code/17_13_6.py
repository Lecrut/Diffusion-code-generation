def get_last_item(d: dict) -> tuple:
    keys = list(d.keys())
    values = list(d.values())
    last_key = keys[-1]
    last_value = values[-1]
    return (last_key, last_value)

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_last_item(sample_dict)
    print(result)