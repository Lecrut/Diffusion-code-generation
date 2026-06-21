def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [12, 45, 78, 34, 21]
    result = calculate_range(sample_numbers)
    print(result)