def calculate_average_grade(grades):
    total_sum = sum(grades)
    count = len(grades)
    if count == 0:
        return 0.0
    return total_sum / count

if __name__ == '__main__':
    student_grades = [85, 90, 78, 92, 88]
    average = calculate_average_grade(student_grades)
    print(average)