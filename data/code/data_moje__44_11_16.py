import statistics

def compute_mean(scores):
    if not isinstance(scores, list):
        raise TypeError('Scores must be provided as a list.')
    if len(scores) == 0:
        raise ValueError('Scores list cannot be empty.')
    for i, score in enumerate(scores):
        if not isinstance(score, (int, float)):
            raise TypeError(f'Element at index {i} is not numeric: {type(score).__name__}')
    return statistics.mean(scores)
if __name__ == '__main__':
    test_scores = [85, 92, 78, 95, 88, 91, 84, 97]
    mean_score = compute_mean(test_scores)
    print(mean_score)