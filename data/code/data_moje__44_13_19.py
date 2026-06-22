def calculate_average(results):
    if not results:
        return 0
    return sum(results) / len(results)

if __name__ == '__main__':
    exam_results = [85, 90, 78, 92, 88]
    result = calculate_average(exam_results)
    print(result)