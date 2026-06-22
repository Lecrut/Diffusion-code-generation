def average_scores(scores):
    if not scores:
        return 0.0
    return sum(score for score in scores) / len(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88, 76, 95, 80]
    result = average_scores(test_scores)
    print(result)