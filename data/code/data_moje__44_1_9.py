def compute_mean(scores):
    if not scores:
        return 0.0
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = compute_mean(test_scores)
    print(result)