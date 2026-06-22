def calculate_mean(scores):
    if not scores:
        return 0.0
    total = 0.0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
        total += score
    return total / len(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    print(calculate_mean(test_scores))
    try:
        invalid_scores = [85, "90", 78]
        print(calculate_mean(invalid_scores))
    except TypeError as e:
        print(e)