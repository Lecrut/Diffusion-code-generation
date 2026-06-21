def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    count = len(numbers)
    total = calculate_sum(numbers)
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        mean_value = calculate_mean(sample_data)
        print(f"The arithmetic mean of {sample_data} is: {mean_value}")
    except ValueError as e:
        print(f"Error encountered: {e}")