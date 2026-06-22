def get_letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
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
    scores = [95, 82, 70, 55, 100, -5, 105]
    for s in scores:
        print(get_letter_grade(s))