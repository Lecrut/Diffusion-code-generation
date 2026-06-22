def average_test_scores():
    scores = [85, 92, 78, 90, 88, 76, 95, 89, 91, 83]
    total = sum(scores)
    count = len(scores)
    if count == 0:
        return 0.0
    return total / count

def average_test_scores_generator(scores):
    if not scores:
        return 0.0
    total = sum(value for value in scores)
    count = sum(1 for _ in scores)
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88, 76, 95, 89, 91, 83]
    result = average_test_scores_generator(sample_scores)
    print(result)