def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    try:
        avg = calculate_average(sample_data)
        print(f"Average of {sample_data}: {avg}")
    except ValueError as e:
        print(f"Error: {e}")