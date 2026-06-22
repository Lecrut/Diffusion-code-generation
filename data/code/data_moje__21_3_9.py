def get_max_value():
    mapping = {
        'a': 5.67,
        'b': 9.12,
        'c': 2.89
    }
    candidates = list(mapping.values())
    largest = candidates[0]
    for val in candidates[1:]:
        if val > largest:
            largest = val
    return largest

if __name__ == '__main__':
    result = get_max_value()
    print(result)