def average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = average(test_scores)
    print(result)