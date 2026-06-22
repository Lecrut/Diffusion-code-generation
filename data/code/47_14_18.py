def get_average_grade():
    grades = [85, 92, 78, 90, 88]
    total_sum = sum(grades)
    count = len(grades)
    average = total_sum / count
    return average

if __name__ == '__main__':
    result = get_average_grade()
    print(result)