def determine_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
if __name__ == '__main__':
    score1 = 95
    score2 = 82
    score3 = 77
    score4 = 55
    score5 = 90
    print(f"Score {score1}: Grade {determine_grade(score1)}")
    print(f"Score {score2}: Grade {determine_grade(score2)}")
    print(f"Score {score3}: Grade {determine_grade(score3)}")
    print(f"Score {score4}: Grade {determine_grade(score4)}")
    print(f"Score {score5}: Grade {determine_grade(score5)}")