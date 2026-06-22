def calculate_mean(test_scores):
    if not test_scores:
        return 0.0
    total = 0
    for score in test_scores:
        total += float(score)
    return total / len(test_scores)

if __name__ == '__main__':
    scores = [85, 90, 78, 92, 88]
    result = calculate_mean(scores)
    print(result)