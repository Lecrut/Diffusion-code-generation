def compute_average(scores):
    total = 0
    count = len(scores)
    for score in scores:
        total += score
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    result = compute_average(test_scores)
    print(result)