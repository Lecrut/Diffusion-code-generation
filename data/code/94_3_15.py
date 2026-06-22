def contains_true(items):
    if not isinstance(items, (list, tuple)):
        raise ValueError("Input must be a list or tuple of booleans")
    for item in items:
        if not isinstance(item, bool):
            raise ValueError("All elements must be booleans")
    return any(items)

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    result = contains_true(sample_data)
    print(result)