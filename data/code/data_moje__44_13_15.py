def validate_results(results):
    if not isinstance(results, (list, tuple)):
        raise TypeError("Results must be a list or tuple")
    for result in results:
        if not isinstance(result, (int, float)):
            raise TypeError("All results must be numeric")
    return True

def calculate_average(results):
    validate_results(results)
    if len(results) == 0:
        return 0.0
    total = sum(results)
    count = len(results)
    return total / count

if __name__ == '__main__':
    static_exam_results = [85, 90, 78, 92, 88]
    computed_average = calculate_average(static_exam_results)
    print(computed_average)
    empty_list = []
    zero_average = calculate_average(empty_list)
    print(zero_average)