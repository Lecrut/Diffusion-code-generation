def find_max_valid_integer(scores):
    max_val = None
    for value in scores:
        if isinstance(value, int) and not isinstance(value, bool):
            if max_val is None or value > max_val:
                max_val = value
    return max_val

if __name__ == '__main__':
    sample_data = (10, 3.5, "85", 92, None, -5, 100, True, 42, "text")
    result = find_max_valid_integer(sample_data)
    print(result)