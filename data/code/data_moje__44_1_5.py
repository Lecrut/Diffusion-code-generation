def compute_mean(scores):
    if not scores:
        return 0.0
    total = sum(scores)
    count = len(scores)
    return total / count

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88, 76, 95, 89, 91, 80]
    result = compute_mean(test_scores)
    print(result)