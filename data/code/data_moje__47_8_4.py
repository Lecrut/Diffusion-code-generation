def calculate_mean(scores):
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
    if len(scores) == 0:
        raise ValueError("Cannot calculate mean of an empty list")
    total = sum(scores)
    mean = total / len(scores)
    return mean

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    mean_value = calculate_mean(sample_scores)
    print(mean_value)

    sample_scores_with_float = [85.5, 90, 78.5, 92, 88]
    mean_value_float = calculate_mean(sample_scores_with_float)
    print(mean_value_float)

    try:
        calculate_mean([85, 90, "invalid"])
    except TypeError as e:
        print(e)

    try:
        calculate_mean([])
    except ValueError as e:
        print(e)