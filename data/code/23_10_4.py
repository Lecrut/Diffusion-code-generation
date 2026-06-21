def score_to_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == '__main__':
    sample_scores = [95, 87, 72, 65, 58, 0, 100, 89, 79, 69, 60]
    for score in sample_scores:
        print(score_to_grade(score))