from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85.5, 90.0, 78.2, 92.1]
    print(calculate_average(sample_scores))