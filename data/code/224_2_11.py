from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    if not scores:
        raise ValueError("Scores list cannot be empty")
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores1 = [85, 92, 78, 88]
    try:
        mean1 = calculate_average(sample_scores1)
        print(f"Mean of {sample_scores1}: {mean1}")
    except ValueError as e:
        print(e)

    sample_scores2 = [10, 20, 30, 40, 50]
    try:
        mean2 = calculate_average(sample_scores2)
        print(f"Mean of {sample_scores2}: {mean2}")
    except ValueError as e:
        print(e)

    sample_scores3 = []
    try:
        mean3 = calculate_average(sample_scores3)
        print(f"Mean of {sample_scores3}: {mean3}")
    except ValueError as e:
        print(e)