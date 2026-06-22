def find_largest_integer_score(scores):
    valid_ints = (score for score in scores if isinstance(score, int) and not isinstance(score, bool))
    largest = None
    for val in valid_ints:
        if largest is None or val > largest:
            largest = val
    return largest

if __name__ == '__main__':
    scores = (10, 25.5, '30', 50, True, -10, 42, None, 100)
    result = find_largest_integer_score(scores)
    print(result)