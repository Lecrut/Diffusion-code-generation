def get_largest_integer_score(scores):
    largest = None
    for score in scores:
        if isinstance(score, int) and not isinstance(score, bool):
            if largest is None or score > largest:
                largest = score
    return largest

if __name__ == '__main__':
    sample_scores = (85, 92.5, "88", 76, None, 95, True, 88)
    result = get_largest_integer_score(sample_scores)
    print(result)