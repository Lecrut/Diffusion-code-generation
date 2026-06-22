from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    if not scores:
        return 0
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85.5, 90.0, 78.2, 92.1]
    average_score = calculate_average(sample_scores)
    print(f"Average score: {average_score}")