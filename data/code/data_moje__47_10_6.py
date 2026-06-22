def calculate_mean(scores):
    if not scores:
        return 0.0
    total = 0
    for score in scores:
        total += float(score)
    return total / len(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = calculate_mean(test_scores)
    print(result)