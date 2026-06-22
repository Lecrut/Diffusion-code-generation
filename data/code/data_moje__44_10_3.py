def average_test_scores(scores):
    if not scores:
        return None
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = average_test_scores(sample_scores)
    print(result)
    empty_scores = []
    result_empty = average_test_scores(empty_scores)
    print(result_empty)