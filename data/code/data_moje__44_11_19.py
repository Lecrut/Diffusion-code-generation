import statistics

def compute_mean(scores: list[float]) -> float:
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85.5, 90.0, 78.5, 92.0, 88.0]
    result = compute_mean(test_scores)
    print(result)