def average_test_scores(scores):
    if not scores:
        raise ValueError('The list of scores is empty.')
    total_sum = sum((score for score in scores))
    count = len(scores)
    return total_sum / count
if __name__ == '__main__':
    predefined_scores = [85, 92, 78, 90, 88, 76, 95, 89, 91, 84]
    avg_score = average_test_scores(predefined_scores)
    print(avg_score)