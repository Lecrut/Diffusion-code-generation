def compute_average(test_scores):
    if not test_scores:
        return 0
    total = 0
    for score in test_scores:
        total += score
    return total / len(test_scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    print(compute_average(sample_scores))