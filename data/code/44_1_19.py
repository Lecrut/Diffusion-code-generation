def compute_mean(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    mean_score = compute_mean(test_scores)
    print(mean_score)