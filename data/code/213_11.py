def analyze_number_set(numbers):
    if not numbers:
        return {
            "even_count": 0,
            "odd_count": 0,
            "sum": 0,
            "min": None,
            "max": None
        }
    even_count = 0
    odd_count = 0
    total_sum = 0
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        total_sum += number
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return {
        "even_count": even_count,
        "odd_count": odd_count,
        "sum": total_sum,
        "min": minimum,
        "max": maximum
    }
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = analyze_number_set(sample_list)
    print(result)
    sample_list_2 = [10, 20, 3, 7, 1]
    result_2 = analyze_number_set(sample_list_2)
    print(result_2)
    sample_list_3 = []
    result_3 = analyze_number_set(sample_list_3)
    print(result_3)