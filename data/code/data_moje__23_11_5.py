def get_grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def convert_scores_to_grades(scores: dict[str, int]) -> dict[str, str]:
    return {name: get_grade(score) for name, score in scores.items()}

if __name__ == '__main__':
    sample_scores = {
        "Alice": 95,
        "Bob": 82,
        "Charlie": 67,
        "Diana": 45
    }
    result = convert_scores_to_grades(sample_scores)
    print(result)