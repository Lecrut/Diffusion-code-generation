def calculate_average():
    grades = [85, 90, 78, 92, 88, 76, 95, 82, 89, 91]
    total = 0
    count = 0
    for grade in grades:
        total = total + grade
        count = count + 1
    average = total / count
    return average

if __name__ == '__main__':
    result = calculate_average()
    print(result)