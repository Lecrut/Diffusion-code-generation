def validate_input(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty")

def calculate_mean(numbers):
    validate_input(numbers)
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    mean_value = calculate_mean(sample_values)
    print(f"Mean of {sample_values}: {mean_value}")