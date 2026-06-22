def average_test_scores():
    scores = [85, 92, 78, 90, 88, 95, 82, 89, 91, 87]
    return sum(score for score in scores) / len(scores)

if __name__ == '__main__':
    result = average_test_scores()
    print(result)