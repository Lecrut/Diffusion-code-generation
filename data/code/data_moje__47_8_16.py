def calculate_mean(scores):
    if not scores:
        return 0.0
    total = 0.0
    count = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [85.5, 90, 78, 92.5, 88]
    sample_scores_with_error = [85.5, 90, "invalid", 78]
    result = calculate_mean(sample_scores)
    print(result)
    try:
        calculate_mean(sample_scores_with_error)
    except TypeError as e:
        print(str(e))