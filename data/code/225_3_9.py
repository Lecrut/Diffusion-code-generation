def calculate_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [10.5, -5.2, 22.3, 0.7, -15.8, 33.4]
    range_result = calculate_range(sample_values)
    print(f"Range: {range_result}")