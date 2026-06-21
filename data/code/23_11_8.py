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

if __name__ == '__main__':
    sample_scores = {"Alice": 95, "Bob": 82, "Charlie": 76, "Diana": 64, "Eve": 55}
    for name, score in sample_scores.items():
        print(f"{name}: {get_grade(score)}")