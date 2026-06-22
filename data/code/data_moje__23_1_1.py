def scores_to_grades(scores):
    grade_boundaries = [
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]
    grade_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'F'}
    results = []
    for score in scores:
        index = 0
        for boundary, _ in grade_boundaries:
            if score < boundary:
                break
            index += 1
        results.append(grade_map[index])
    return results

if __name__ == '__main__':
    raw_scores = [95, 82, 71, 65, 58, 100]
    letter_grades = scores_to_grades(raw_scores)
    print(letter_grades)