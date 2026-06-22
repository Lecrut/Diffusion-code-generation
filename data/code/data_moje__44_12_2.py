def average_scores(scores):
    if not scores:
        return 0.0
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88, 76, 95, 84, 91, 87]
    result = average_scores(test_scores)
    print(result)