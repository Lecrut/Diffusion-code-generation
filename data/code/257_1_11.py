def calculate_difference(numbers):
    if not numbers:
        raise ValueError("The tuple must contain at least one number.")
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    print(calculate_difference(sample_values))