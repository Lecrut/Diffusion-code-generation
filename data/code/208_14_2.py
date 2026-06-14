def calculate_arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    empty_data = []
    try:
        mean_result = calculate_arithmetic_mean(sample_data)
        print(f"The arithmetic mean of {sample_data} is: {mean_result}")
        mean_result_empty = calculate_arithmetic_mean(empty_data)
    except ValueError as e:
        print(f"Error encountered: {e}")