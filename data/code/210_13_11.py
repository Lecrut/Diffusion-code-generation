def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [4, 9, 2, 5, 6]
    range_value = calculate_range(sample_numbers)
    print(range_value)