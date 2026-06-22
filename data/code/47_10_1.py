def calculate_arithmetic_mean(scores):
    if not scores:
        raise ValueError("The list of scores is empty.")
    total = 0.0
    count = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All scores must be numeric.")
        total += float(score)
        count += 1
    return total / count

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = calculate_arithmetic_mean(test_scores)
    print(result)