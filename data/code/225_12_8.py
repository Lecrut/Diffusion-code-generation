def find_min_max(data):
    min_val = min((value for value in data.values() if isinstance(value, (int, float))), default=None)
    max_val = max((value for value in data.values() if isinstance(value, (int, float))), default=None)
    return (min_val, max_val)

if __name__ == '__main__':
    sample_data = {
        'a': 3,
        'b': 1,
        'c': 4.5,
        'd': -2
    }
    result = find_min_max(sample_data)
    print(result)