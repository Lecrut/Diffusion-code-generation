from typing import Iterable

def calculate_average(scores: Iterable[float]) -> float:
    if not scores:
        raise ValueError("The iterable of scores cannot be empty.")
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85.5, 90.0, 78.2, 92.1]
    try:
        average_score = calculate_average(sample_scores)
        print(f"The average score of {sample_scores} is: {average_score}")
    except ValueError as e:
        print(e)