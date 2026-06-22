def get_grade(score):
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return "Invalid"
    grade_boundaries = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
    for threshold, letter in grade_boundaries:
        if score >= threshold:
            return letter
    return "F"

if __name__ == '__main__':
    sample_scores = [100, 90, 89, 80, 79, 70, 69, 60, 59, 0, 101, -1]
    for s in sample_scores:
        print(f"{s}: {get_grade(s)}")