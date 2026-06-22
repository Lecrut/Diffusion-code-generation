from typing import Final

BOUNDARIES: Final[list[float]] = [0.0, 60.0, 70.0, 80.0, 90.1, 100.0]
GRADES: Final[list[str]] = ["F", "D", "C", "B", "A"]

def calculate_grade(score: float) -> str:
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0.0 or score > 100.0:
        raise ValueError("Score must be between 0 and 100 inclusive")
    for i in range(len(GRADES) - 1, -1, -1):
        if score >= BOUNDARIES[i + 1]:
            return GRADES[i]
    return GRADES[0]

if __name__ == '__main__':
    sample_scores: list[float] = [0.0, 59.99, 60.0, 69.99, 70.0, 79.99, 80.0, 89.99, 90.1, 100.0]
    for s in sample_scores:
        print(calculate_grade(s))