def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4)
    print(f"Mean of {sample_values}: {calculate_mean(sample_values)}")