def average_of_grades():
    grades = [85, 92, 78, 90, 88]
    total = sum(grades)
    count = len(grades)
    return total / count

if __name__ == '__main__':
    print(average_of_grades())