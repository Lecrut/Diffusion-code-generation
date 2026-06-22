def average_of_constant_grades():
    grades = [85, 92, 78, 90, 88]
    total_sum = sum(grades)
    count = len(grades)
    return total_sum / count

if __name__ == '__main__':
    print(average_of_constant_grades())