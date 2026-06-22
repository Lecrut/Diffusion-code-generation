def average_test_scores(scores):
    if not scores:
        return 0.0
    return sum(score for score in scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88, 95, 82, 89, 91, 87]
    result = average_test_scores(sample_scores)
    print(result)