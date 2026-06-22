def average_test_scores():
    scores = [85, 92, 78, 95, 88, 76, 91, 83, 89, 94]
    return sum(score for score in scores) / len(scores)

if __name__ == '__main__':
    print(average_test_scores())