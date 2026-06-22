def average_test_scores(scores):
    if not scores:
        return 0.0
    total = sum(x for x in scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    result = average_test_scores(sample_scores)
    print(result)