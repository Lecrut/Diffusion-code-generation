def calculate_median(numbers):
    n = len(numbers)
    if n == 0:
        raise ValueError("The list is empty")
    
    sorted_numbers = sorted(numbers)
    middle_index = n // 2
    
    if n % 2 != 0:
        return sorted_numbers[middle_index]
    else:
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 7]
    try:
        median_value = calculate_median(sample_data)
        print(f"The median is: {median_value}")
    except ValueError as e:
        print(e)