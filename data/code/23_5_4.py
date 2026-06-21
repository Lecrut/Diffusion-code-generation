def scores_to_grades(scores):
    return ['A' if s >= 90 else 'B' if s >= 80 else 'C' if s >= 70 else 'D' if s >= 60 else 'F' for s in scores]

if __name__ == '__main__':
    sample_scores = [95, 82, 76, 64, 45, 100, 0]
    print(scores_to_grades(sample_scores))