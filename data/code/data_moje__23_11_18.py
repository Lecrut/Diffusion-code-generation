from typing import Dict

SCORE_THRESHOLDS: Dict[str, int] = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0,
}

def calculate_grade(score: int) -> str:
    for grade, threshold in SCORE_THRESHOLDS.items():
        if score >= threshold:
            return grade
    return "F"

SCORES: Dict[str, int] = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 76,
    "Diana": 58,
}

if __name__ == "__main__":
    for name, score in SCORES.items():
        grade = calculate_grade(score)
        print(f"{name}: {grade}")