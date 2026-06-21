def calculate_arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    total = 0.0
    count = len(numbers)
    for number in numbers:
        total += number
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    empty_data = []
    try:
        mean_value = calculate_arithmetic_mean(sample_data)
        print(f"The arithmetic mean of {sample_data} is: {mean_value}")
    except ValueError as e:
        print(f"Error encountered: {e}")