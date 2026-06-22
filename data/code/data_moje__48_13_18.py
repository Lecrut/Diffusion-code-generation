def find_largest_valid_integer(scores):
    largest = None
    for item in scores:
        if isinstance(item, int) and not isinstance(item, bool):
            if largest is None or item > largest:
                largest = item
    return largest

if __name__ == '__main__':
    sample_scores = (42, 3.14, "hello", -7, 100, True, None, 55, 0, -1, "world", 99.9)
    result = find_largest_valid_integer(sample_scores)
    print(result)