def get_grade(score):
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
    test_scores = [95, 82, 76, 65, 49, 101, -5]
    for s in test_scores:
        print(get_grade(s))