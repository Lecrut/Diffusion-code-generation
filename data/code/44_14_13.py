def compute_average(scores):
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = compute_average(test_scores)
    print(result)