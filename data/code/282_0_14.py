def calculate_total(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be integers or floats.")
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 25, 40, 5]
    total_sum = calculate_total(sample_numbers)
    print(total_sum)