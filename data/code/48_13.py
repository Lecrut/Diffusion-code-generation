def get_largest_valid_score(scores):
    valid_integers = (x for x in scores if isinstance(x, int) and not isinstance(x, bool))
    largest = None
    for val in valid_integers:
        if largest is None or val > largest:
            largest = val
    return largest

if __name__ == '__main__':
    scores = (10, 25.5, 3, 'a', -1, 100, True, 0, -50, None)
    result = get_largest_valid_score(scores)
    print(result)