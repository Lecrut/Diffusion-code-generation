def calculate_average(scores):
    total = sum(score for score in scores)
    count = len(scores)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = calculate_average(test_scores)
    print(result)