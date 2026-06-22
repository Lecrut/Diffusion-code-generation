import statistics

def compute_mean(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty")
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 92, 78, 90, 88]
    result = compute_mean(test_scores)
    print(result)