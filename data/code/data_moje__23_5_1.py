def scores_to_grades(scores):
    return [
        'A' if s >= 90 else
        'B' if s >= 80 else
        'C' if s >= 70 else
        'D' if s >= 60 else
        'F'
        for s in scores
    ]

if __name__ == '__main__':
    sample_scores = [92, 85, 73, 68, 55, 88, 91, 79, 60, 45]
    grades = scores_to_grades(sample_scores)
    print(grades)