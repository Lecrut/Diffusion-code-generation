import statistics

def compute_mean_of_test_scores(scores: list[float]) -> float:
    if not isinstance(scores, list) or len(scores) == 0:
        raise ValueError("Scores must be a non-empty list of numbers")
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError(f"All scores must be numeric, got {type(score).__name__}")
    return statistics.mean(scores)

if __name__ == '__main__':
    hardcoded_scores = [85.5, 92.0, 78.5, 95.0, 88.0]
    mean_value = compute_mean_of_test_scores(hardcoded_scores)
    print(mean_value)