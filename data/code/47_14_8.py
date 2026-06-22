def calculate_average_grades():
    grades = [85, 92, 78, 90, 88]
    total_sum = sum(grades)
    count = len(grades)
    average = total_sum / count
    return average

if __name__ == '__main__':
    result = calculate_average_grades()
    print(result)