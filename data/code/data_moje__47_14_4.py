def average_student_grades():
    grades = [85, 90, 78, 92, 88]
    total = sum(grades)
    count = len(grades)
    result = total / count
    return result

if __name__ == '__main__':
    avg = average_student_grades()
    print(avg)