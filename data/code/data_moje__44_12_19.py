def average_test_scores(scores):
    if not scores:
        raise ValueError("List of scores is empty")
    total = sum(score for score in scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = average_test_scores(sample_scores)
    print(result)