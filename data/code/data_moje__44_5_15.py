def average_test_scores(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = average_test_scores(sample_scores)
    print(result)