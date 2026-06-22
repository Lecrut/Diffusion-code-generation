def average_score(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    print(average_score(test_scores))