import statistics

def compute_mean(scores: list[float]) -> float:
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = [85, 90, 92, 88, 95]
    result = compute_mean(test_scores)
    print(result)