def calculate_total_sum(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 25, 5, 42, 18]
    try:
        total_sum = calculate_total_sum(sample_numbers)
        print(total_sum)
    except ValueError as e:
        print(e)