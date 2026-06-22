def average_of_test_scores():
    test_scores = [85, 92, 78, 90, 88]
    total = 0
    for score in test_scores:
        total += score
    count = len(test_scores)
    result = total / count
    return result

if __name__ == '__main__':
    print(average_of_test_scores())