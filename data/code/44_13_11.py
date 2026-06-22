def calculate_average(results):
    if not results:
        return 0
    total = sum(results)
    count = len(results)
    return total / count

if __name__ == '__main__':
    exam_results = [85, 90, 78, 92, 88]
    average = calculate_average(exam_results)
    print(average)