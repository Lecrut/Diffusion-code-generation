def calculate_mean(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [1.5, 2.5, 3.0, 4.0, 5.5]
    result = calculate_mean(sample_data)
    print(result)