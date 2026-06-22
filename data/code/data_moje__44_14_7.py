def compute_average_scores(scores):
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    result = compute_average_scores(test_scores)
    print(result)