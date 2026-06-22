def find_max_integer(values):
    max_val = None
    for value in values:
        if isinstance(value, int) and not isinstance(value, bool):
            if max_val is None or value > max_val:
                max_val = value
    return max_val

if __name__ == '__main__':
    scores = (10, 25.5, 30, 'invalid', 45, 12, True, 8.9, 50, -5)
    result = find_max_integer(scores)
    print(result)