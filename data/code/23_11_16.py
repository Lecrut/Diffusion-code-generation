def get_grade(score: int) -> str:
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

def grade_map(scores: dict[str, int]) -> dict[str, str]:
    return {name: get_grade(score) for name, score in scores.items()}

if __name__ == '__main__':
    sample_scores = {"Alice": 95, "Bob": 82, "Charlie": 67, "Diana": 59}
    results = grade_map(sample_scores)
    for name, grade in results.items():
        print(f"{name}: {grade}")