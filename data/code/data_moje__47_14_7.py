def average_grades(grades):
    total_sum = sum(grades)
    count = len(grades)
    return total_sum / count

if __name__ == '__main__':
    sample_grades = [85, 90, 78, 92, 88]
    result = average_grades(sample_grades)
    print(result)