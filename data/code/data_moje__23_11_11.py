def get_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def grade_scores(scores_dict):
    return {name: get_grade(score) for name, score in scores_dict.items()}

if __name__ == '__main__':
    sample_scores = {
        "Alice": 95,
        "Bob": 82,
        "Charlie": 74,
        "Diana": 58,
        "Evan": 89
    }
    print(grade_scores(sample_scores))