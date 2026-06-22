from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    print(calculate_average(sample_scores))