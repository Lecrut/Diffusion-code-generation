def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = (3, 5, 7, 9)
    result = calculate_mean(sample_values)
    print(result)