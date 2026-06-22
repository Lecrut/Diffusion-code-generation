def get_average_grade(grades):
    total_sum = sum(grades)
    count = len(grades)
    return total_sum / count

if __name__ == '__main__':
    student_grades = [85, 90, 78, 92, 88]
    result = get_average_grade(student_grades)
    print(result)