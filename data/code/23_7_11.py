def get_grade(score, score_grade_pairs):
    sorted_pairs = sorted(score_grade_pairs, key=lambda x: x[0])
    idx = 0
    for s, g in sorted_pairs:
        if score >= s:
            idx = s
        else:
            break
    for s, g in sorted_pairs:
        if s == idx:
            return g
    return sorted_pairs[0][1]

if __name__ == '__main__':
    score_grade_pairs = [
        (0, 'F'),
        (60, 'D'),
        (70, 'C'),
        (80, 'B'),
        (90, 'A')
    ]
    score = 85
    result = get_grade(score, score_grade_pairs)
    print(result)