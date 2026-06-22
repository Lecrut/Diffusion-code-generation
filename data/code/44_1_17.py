def compute_mean(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = compute_mean(sample_scores)
    print(result)