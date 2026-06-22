def calculate_average_grades():
    grades = [85, 90, 78, 92, 88]
    total_sum = sum(grades)
    count = len(grades)
    average = total_sum / count
    return average

if __name__ == '__main__':
    print(calculate_average_grades())