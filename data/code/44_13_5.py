def calculate_average(results):
    if not results:
        return 0.0
    return sum(results) / len(results)

if __name__ == '__main__':
    exam_results = [85, 92, 78, 95, 88]
    average_score = calculate_average(exam_results)
    print(average_score)