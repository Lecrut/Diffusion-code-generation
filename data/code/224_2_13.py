from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    if not scores:
        raise ValueError("Score list is empty")
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85.5, 90.0, 78.2, 92.1]
    try:
        avg_score = calculate_average(sample_scores)
        print(f"Average of {sample_scores}: {avg_score}")
    except ValueError as e:
        print(e)