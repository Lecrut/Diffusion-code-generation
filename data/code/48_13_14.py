def filter_and_find_max(scores):
    valid_integers = [score for score in scores if isinstance(score, int) and not isinstance(score, bool)]
    if not valid_integers:
        return None
    max_value = valid_integers[0]
    for value in valid_integers[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_scores = (10, 20.5, 30, '40', 5, True, 100, None, -5, 50.0, 75)
    result = filter_and_find_max(sample_scores)
    print(result)