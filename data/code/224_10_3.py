def calculate_mean(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    try:
        mean_value = calculate_mean(sample_values)
        print(f"Mean of {sample_values}: {mean_value}")
    except ValueError as e:
        print(e)