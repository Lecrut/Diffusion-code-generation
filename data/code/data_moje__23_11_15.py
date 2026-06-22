SCORE_RANGES = {
    'A': (90, 100),
    'B': (80, 89),
    'C': (70, 79),
    'D': (60, 69),
    'F': (0, 59)
}

def get_grade(score: int) -> str:
    if score > 100 or score < 0:
        raise ValueError("Score must be between 0 and 100.")
    for grade, (low, high) in SCORE_RANGES.items():
        if low <= score <= high:
            return grade
    return 'F'

def calculate_grades(scores: dict[str, int]) -> dict[str, str]:
    return {name: get_grade(s) for name, s in scores.items()}

if __name__ == '__main__':
    student_scores = {
        'Alice': 95,
        'Bob': 82,
        'Charlie': 71,
        'David': 55,
        'Eve': 100
    }
    result = calculate_grades(student_scores)
    for name, grade in result.items():
        print(f"{name}: {grade}")