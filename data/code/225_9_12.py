def find_min_max(values):
    if not values:
        return None, None
    min_val = max_val = next(iter(values.values()))
    for val in values.values():
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    return min_val, max_val

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 5,
        'c': 20,
        'd': 3
    }
    print(find_min_max(sample_values))