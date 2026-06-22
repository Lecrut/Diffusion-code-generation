def get_letter_grades(raw_scores):
    grade_boundaries = {
        90: 'A',
        80: 'B',
        70: 'C',
        60: 'D',
        0: 'F'
    }
    sorted_boundaries = sorted(grade_boundaries.keys(), reverse=True)
    letter_map = {boundary: grade_boundaries[boundary] for boundary in sorted_boundaries}

    result = []
    for score in raw_scores:
        for boundary in sorted_boundaries:
            if score >= boundary:
                result.append(letter_map[boundary])
                break
        else:
            result.append('F')
    return result

if __name__ == '__main__':
    sample_scores = [95, 82, 74, 68, 59, 100, 50]
    grades = get_letter_grades(sample_scores)
    print(grades)