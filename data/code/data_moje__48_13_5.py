def find_max_valid_score(scores):
    max_value = None
    for score in scores:
        if isinstance(score, int) and not isinstance(score, bool):
            if max_value is None or score > max_value:
                max_value = score
    return max_value

if __name__ == '__main__':
    sample_scores = (10, 20.5, '88', 95, None, 3, True, 7)
    result = find_max_valid_score(sample_scores)
    print(result)