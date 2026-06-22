def calculate_mean(scores):
    if not scores:
        return 0.0
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return float(total) / count

if __name__ == '__main__':
    test_scores = [85.5, 90.0, 78.5, 92.0, 88.0]
    result = calculate_mean(test_scores)
    print(result)