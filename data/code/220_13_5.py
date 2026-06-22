def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [42, 35, 28]
    print(calculate_average(sample_numbers))