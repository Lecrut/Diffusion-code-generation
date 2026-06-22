def average_test_scores():
    scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
    return sum(x for x in scores) / len(scores)

if __name__ == '__main__':
    result = average_test_scores()
    print(result)