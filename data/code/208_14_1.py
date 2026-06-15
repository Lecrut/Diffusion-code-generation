def calculate_arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    empty_data = []
    print(f"Sample Data: {sample_data}")
    try:
        mean_value = calculate_arithmetic_mean(sample_data)
        print(f"The arithmetic mean of the sample data is: {mean_value}")
    except ValueError as e:
        print(f"Error calculating mean for sample data: {e}")
    print("\nTesting with empty list:")
    try:
        calculate_arithmetic_mean(empty_data)
    except ValueError as e:
        print(f"Successfully caught expected error: {e}")