def calculate_arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        mean_value = calculate_arithmetic_mean(sample_data)
        print(f"The arithmetic mean of {sample_data} is: {mean_value}")
    except ValueError as e:
        print(f"Error encountered: {e}")