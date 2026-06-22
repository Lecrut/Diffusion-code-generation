def calculate_average_grade(grades):
    if len(grades) == 0:
        return 0
    total_sum = sum(grades)
    count = len(grades)
    return total_sum / count

if __name__ == '__main__':
    sample_grades = [85, 90, 78, 92, 88]
    result = calculate_average_grade(sample_grades)
    print(result)