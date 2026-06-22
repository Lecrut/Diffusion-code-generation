def find_largest_valid_integer(scores: tuple) -> int | None:
    max_val = None
    for score in scores:
        if isinstance(score, int) and not isinstance(score, bool):
            if max_val is None or score > max_val:
                max_val = score
    return max_val

if __name__ == '__main__':
    scores_data = (10, 3.14, -5, "invalid", 42, 0, 99, True, None, 77)
    result = find_largest_valid_integer(scores_data)
    print(result)