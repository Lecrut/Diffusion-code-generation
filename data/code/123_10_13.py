def calculate_total_sum(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a list of integers")
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 6, 9, 12]
    total_sum = calculate_total_sum(sample_numbers)
    print(total_sum)