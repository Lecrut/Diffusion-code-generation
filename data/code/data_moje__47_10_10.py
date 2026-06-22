def calculate_mean(scores):
    if not scores:
        return 0.0
    total = 0.0
    for score in scores:
        total += float(score)
    return total / len(scores)

if __name__ == '__main__':
    test_scores = [85, 92, 78, 95, 88]
    result = calculate_mean(test_scores)
    print(result)