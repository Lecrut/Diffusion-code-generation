def calculate_sum(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers")
    return sum(numbers)

if __name__ == '__main__':
    sample_list = [1, 5, 10, -3, 8]
    result = calculate_sum(sample_list)
    print(result)
    empty_list = []
    result_empty = calculate_sum(empty_list)
    print(result_empty)