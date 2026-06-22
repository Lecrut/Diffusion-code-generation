def calculate_average(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

if __name__ == '__main__':
    exam_results = [85, 90, 78, 92, 88]
    print(calculate_average(exam_results))
    print(calculate_average([]))