def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [45, 23, 78, 12, 65]
    result = calculate_range(sample_values)
    print(result)