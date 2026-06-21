def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be integers or floats")

def sum_of_elements(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

if __name__ == '__main__':
    sample_list1 = [1, -2, 3, -4, 5]
    validate_numbers(sample_list1)
    result1 = sum_of_elements(sample_list1)
    print(f"Result for {sample_list1}: {result1}")

    sample_list2 = [-10, 0, 5, -2.5]
    validate_numbers(sample_list2)
    result2 = sum_of_elements(sample_list2)
    print(f"Result for {sample_list2}: {result2}")