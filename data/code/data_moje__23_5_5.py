def scores_to_grades(scores):
    return ['A' if s >= 90 else 'B' if s >= 80 else 'C' if s >= 70 else 'D' if s >= 60 else 'F' for s in scores]

if __name__ == '__main__':
    print(scores_to_grades([95, 82, 70, 55, 100]))