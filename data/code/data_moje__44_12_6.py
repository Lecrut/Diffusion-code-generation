def calculate_average(scores):
    if not scores:
        return 0
    return sum(score for score in scores) / len(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    print(calculate_average(test_scores))