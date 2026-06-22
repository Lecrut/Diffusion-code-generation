def find_largest_valid_integer(scores):
    largest = None
    for item in scores:
        if isinstance(item, int) and not isinstance(item, bool):
            if largest is None or item > largest:
                largest = item
    return largest

if __name__ == '__main__':
    sample_scores = (42, 3.14, "hello", 7, -15, 100, None, 3.14, True, 99)
    result = find_largest_valid_integer(sample_scores)
    print(result)