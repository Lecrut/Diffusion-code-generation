def compute_grades(scores):
    grades = []
    for s in scores:
        if s >= 90:
            grades.append('A')
        elif s >= 80:
            grades.append('B')
        elif s >= 70:
            grades.append('C')
        elif s >= 60:
            grades.append('D')
        else:
            grades.append('F')
    return grades

if __name__ == '__main__':
    sample_scores = [95, 82, 71, 55, 40]
    result = compute_grades(sample_scores)
    print(result)