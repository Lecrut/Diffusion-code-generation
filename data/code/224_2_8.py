from typing import Iterable

def validate_scores(scores: Iterable[float]) -> None:
    if not all(isinstance(score, (int, float)) for score in scores):
        raise ValueError("All elements in the scores iterable must be numbers.")

def calculate_average(scores: Iterable[float]) -> float:
    validate_scores(scores)
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores1 = [85, 92, 78, 88]
    avg1 = calculate_average(sample_scores1)
    print(f"Average of {sample_scores1}: {avg1}")
    
    sample_scores2 = [10, 20, 30, 40, 50]
    avg2 = calculate_average(sample_scores2)
    print(f"Average of {sample_scores2}: {avg2}")
    
    sample_scores3 = []
    try:
        avg3 = calculate_average(sample_scores3)
        print(f"Average of {sample_scores3}: {avg3}")
    except ValueError as e:
        print(e)