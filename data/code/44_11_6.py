import statistics
import typing

def compute_mean(scores: typing.Sequence[float]) -> float:
    if not scores:
        raise ValueError('The sequence of scores must not be empty.')
    validated_scores: list[float] = []
    for idx, score in enumerate(scores):
        if not isinstance(score, (int, float)):
            raise TypeError(f'Score at index {idx} is of type {type(score).__name__}, expected int or float.')
        if isinstance(score, bool):
            raise TypeError(f'Score at index {idx} is a boolean, which is not a valid numeric type for this calculation.')
        validated_scores.append(float(score))
    return statistics.mean(validated_scores)
if __name__ == '__main__':
    sample_scores = [85.5, 90.0, 78.5, 92.0, 88.5]
    result = compute_mean(sample_scores)
    print(result)