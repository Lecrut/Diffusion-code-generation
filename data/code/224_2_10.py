from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    total = sum(scores)
    count = len(scores)
    return total / count if count > 0 else 0.0

if __name__ == '__main__':
    sample_scores = [85.5, 92.3, 78.4, 90.1]
    average_score = calculate_average(sample_scores)
    print(f"The average score is: {average_score:.2f}")