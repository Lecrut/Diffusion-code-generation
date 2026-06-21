from typing import Dict, Tuple, List, Union

def get_grade(score: int, thresholds: Dict[str, Tuple[int, int]]) -> str:
    grade_order = ["A", "B", "C", "D", "F"]
    for grade in grade_order:
        if grade in thresholds:
            min_score, max_score = thresholds[grade]
            if min_score <= score <= max_score:
                return grade
    return "F"

if __name__ == '__main__':
    custom_thresholds = {
        "A": (90, 100),
        "B": (80, 89),
        "C": (70, 79),
        "D": (60, 69),
        "F": (0, 59)
    }
    result = get_grade(92, custom_thresholds)
    print(result)