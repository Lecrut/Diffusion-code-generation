def average_test_scores():
    scores = [85, 92, 78, 90, 88, 76, 95, 89, 91, 83]
    total = sum(score for score in scores)
    count = sum(1 for _ in scores)
    return total / count if count > 0 else 0.0

if __name__ == '__main__':
    result = average_test_scores()
    print(result)