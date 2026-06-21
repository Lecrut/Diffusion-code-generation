def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 2, 8, 4, 6]
    range_value = calculate_range(sample_numbers)
    print(f"The range of {sample_numbers} is {range_value}")