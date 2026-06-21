def scores_to_grades(raw_scores):
    score_map = {
        range(90, 101): 'A',
        range(80, 90): 'B',
        range(70, 80): 'C',
        range(60, 70): 'D',
        range(-1, 60): 'F'
    }
    
    grades = []
    for score in raw_scores:
        for score_range, grade in score_map.items():
            if score in score_range:
                grades.append(grade)
                break
    
    return grades

if __name__ == '__main__':
    raw_scores_list = [95, 82, 76, 65, 59, 100]
    result = scores_to_grades(raw_scores_list)
    print(result)