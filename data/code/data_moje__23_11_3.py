SCORES = {
    "alice": 92,
    "bob": 85,
    "charlie": 76,
    "diana": 68,
    "eve": 45
}

GRADE_BOUNDARIES = [
    (90, 'A'),
    (80, 'B'),
    (70, 'C'),
    (60, 'D'),
    (0, 'F')
]

def calculate_grades(scores: dict[str, int]) -> dict[str, str]:
    result = {}
    for name, score in scores.items():
        grade = 'F'
        for boundary, letter in GRADE_BOUNDARIES:
            if score >= boundary:
                grade = letter
                break
        result[name] = grade
    return result

if __name__ == '__main__':
    grades = calculate_grades(SCORES)
    for name in grades:
        print(f"{name}: {grades[name]}")