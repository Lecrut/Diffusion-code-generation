def calculate_average_grade(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

if __name__ == '__main__':
    student_grades = [85, 90, 78, 92, 88]
    average = calculate_average_grade(student_grades)
    print(average)