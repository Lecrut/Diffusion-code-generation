def calculate_arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    empty_data = []
    print("Sample Data:", sample_data)
    try:
        mean_value = calculate_arithmetic_mean(sample_data)
        print("Arithmetic Mean of Sample Data:", mean_value)
    except ValueError as e:
        print("Error calculating mean for sample data:", e)
    print("\nTesting with Empty List:")
    try:
        calculate_arithmetic_mean(empty_data)
    except ValueError as e:
        print("Successfully caught expected error for empty list:", e)