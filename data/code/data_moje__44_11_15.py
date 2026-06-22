import statistics

def compute_mean(test_scores: list) -> float:
    if not isinstance(test_scores, list):
        raise TypeError("test_scores must be a list")
    for score in test_scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All elements must be numeric")
    if len(test_scores) == 0:
        raise ValueError("test_scores must not be empty")
    return statistics.mean(test_scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = compute_mean(sample_scores)
    print(result)