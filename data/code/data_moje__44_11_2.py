import statistics

def compute_mean(scores: list[float]) -> float:
    if not isinstance(scores, list):
        raise TypeError('scores must be a list')
    if len(scores) == 0:
        raise ValueError('scores must not be empty')
    for i, score in enumerate(scores):
        if not isinstance(score, (int, float)):
            raise TypeError(f'All elements must be numeric; index {i} has type {type(score).__name__}')
    return statistics.mean(scores)
if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    result = compute_mean(sample_scores)
    print(result)