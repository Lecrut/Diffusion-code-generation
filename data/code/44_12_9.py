def average_test_scores():
    scores = [85, 90, 78, 92, 88, 95, 82, 91, 76, 89]
    return sum(score for score in scores) / len(scores)

if __name__ == '__main__':
    result = average_test_scores()
    print(result)