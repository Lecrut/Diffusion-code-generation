def calculate_mean(scores):
    total = 0
    count = 0
    for score in scores:
        if isinstance(score, bool):
            raise TypeError("Non-numeric element found")
        if not isinstance(score, (int, float)):
            raise TypeError("Non-numeric element found")
        total += score
        count += 1
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(test_scores)
    print(result)