score_to_grade = {0: 'F', 1: 'F', 2: 'F', 3: 'F', 4: 'F', 5: 'F', 55: 'F', 59: 'F', 60: 'D', 69: 'D', 70: 'C', 79: 'C', 80: 'B', 89: 'B', 90: 'A', 100: 'A'}

def get_grade(score):
    if score >= 90:
        return score_to_grade[100]
    if score >= 80:
        return score_to_grade[89]
    if score >= 70:
        return score_to_grade[79]
    if score >= 60:
        return score_to_grade[69]
    return score_to_grade[59]

if __name__ == '__main__':
    raw_scores = [95, 82, 76, 61, 58, 45, 100, 0]
    grades = [get_grade(s) for s in raw_scores]
    print(grades)