import statistics

def compute_mean(scores: list[float]) -> float:
    if not scores:
        raise ValueError('Scores list must not be empty.')
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError(f'All scores must be numeric, got {type(score).__name__}')
        if isinstance(score, bool):
            raise TypeError(f'All scores must be numeric, got bool')
    return statistics.mean(scores)
if __name__ == '__main__':
    sample_scores = [85.5, 92.0, 78.5, 95.0, 88.0]
    result = compute_mean(sample_scores)
    print(result)