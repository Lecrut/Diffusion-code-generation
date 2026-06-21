def calculate_arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    try:
        mean_value = calculate_arithmetic_mean(sample_data)
        print(f"The arithmetic mean of {sample_data} is: {mean_value}")
    except ValueError as e:
        print(f"Error encountered: {e}")