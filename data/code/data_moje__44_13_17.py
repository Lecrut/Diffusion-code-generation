def calculate_average(results):
    if not results:
        return 0.0
    total = sum(results)
    count = len(results)
    return total / count

if __name__ == '__main__':
    exam_results = [85, 92, 78, 90, 88, 76, 95, 82]
    average = calculate_average(exam_results)
    print(average)