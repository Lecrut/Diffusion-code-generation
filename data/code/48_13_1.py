def find_max_valid_integer(data):
    max_value = None
    for item in data:
        if isinstance(item, int) and not isinstance(item, bool):
            if max_value is None or item > max_value:
                max_value = item
    return max_value

if __name__ == '__main__':
    scores = (10, 3.5, "99", 20, None, 15, True, 8, 25.0, 42)
    result = find_max_valid_integer(scores)
    print(result)