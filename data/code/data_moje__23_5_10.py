def calculate_grades(scores):
    return [chr(65 + (100 - score) // 10) if score >= 60 else 'F' for score in scores]

if __name__ == '__main__':
    scores = [85, 55, 92, 40, 70]
    grades = calculate_grades(scores)
    print(grades)