def find_max_valid_integer(scores):
    max_value = None
    for item in scores:
        if isinstance(item, int) and not isinstance(item, bool):
            if max_value is None or item > max_value:
                max_value = item
    return max_value

if __name__ == '__main__':
    sample_scores = (10, "85", 3.14, 42, "valid", 17, True, 99, None)
    result = find_max_valid_integer(sample_scores)
    print(result)