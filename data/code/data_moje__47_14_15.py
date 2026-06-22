def calculate_average_grade():
    grades = [85, 92, 78, 95, 88]
    total = 0
    for grade in grades:
        total = total + grade
    count = len(grades)
    average = total / count
    return average

if __name__ == '__main__':
    result = calculate_average_grade()
    print(result)