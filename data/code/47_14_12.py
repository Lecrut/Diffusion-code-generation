def average_grade():
    grades = [85, 90, 78, 92, 88]
    total = sum(grades)
    count = len(grades)
    return total / count

if __name__ == '__main__':
    result = average_grade()
    print(result)