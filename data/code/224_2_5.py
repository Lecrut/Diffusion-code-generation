from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    if not scores:
        return 0
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average

if __name__ == '__main__':
    sample_scores1 = [85.5, 92.3, 78.4, 88.1]
    mean_score1 = calculate_average(sample_scores1)
    print(f"Mean of {sample_scores1}: {mean_score1}")

    sample_scores2 = [10.0, 20.5, 30.0, 40.25, 50.75]
    mean_score2 = calculate_average(sample_scores2)
    print(f"Mean of {sample_scores2}: {mean_score2}")

    sample_scores3 = []
    mean_score3 = calculate_average(sample_scores3)
    print(f"Mean of {sample_scores3}: {mean_score3}")