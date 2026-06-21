def convert_scores_to_grades(scores):
    grades = []
    for score in scores:
        if score >= 90:
            grades.append('A')
        elif score >= 80:
            grades.append('B')
        elif score >= 70:
            grades.append('C')
        elif score >= 60:
            grades.append('D')
        else:
            grades.append('F')
    return grades

if __name__ == '__main__':
    sample_scores = [92, 85, 73, 61, 45, 89, 100, 59, 78, 60]
    result = convert_scores_to_grades(sample_scores)
    print(result)