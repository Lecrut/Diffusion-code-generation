def average_grades(grades):
    total_sum = sum(grades)
    count = len(grades)
    average = total_sum / count
    return average

if __name__ == '__main__':
    student_grades = [85, 90, 78, 92, 88]
    result = average_grades(student_grades)
    print(result)