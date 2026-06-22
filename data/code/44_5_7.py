def compute_average(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = compute_average(test_scores)
    print(result)