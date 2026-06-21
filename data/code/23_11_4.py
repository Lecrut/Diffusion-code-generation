from typing import Dict, List, Tuple

def calculate_grades(scores: Dict[str, float]) -> List[Tuple[str, str]]:
    def get_grade(score: float) -> str:
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    return [(student, get_grade(score)) for student, score in scores.items()]

if __name__ == '__main__':
    sample_scores = {
        "Alice": 95.5,
        "Bob": 82.0,
        "Charlie": 74.5,
        "Diana": 68.0,
        "Eve": 45.0
    }
    results = calculate_grades(sample_scores)
    for student, grade in results:
        print(f"{student}: {grade}")