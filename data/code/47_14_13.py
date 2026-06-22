def calculate_average_grade(grades):
    total = sum(grades)
    count = len(grades)
    if count == 0:
        return 0
    return total / count

if __name__ == "__main__":
    student_grades = [85, 90, 78, 92, 88]
    result = calculate_average_grade(student_grades)
    print(result)