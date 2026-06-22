def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        raise ValueError("The list cannot be empty")
    return total / count

if __name__ == '__main__':
    sample_values = [12, 24, 36, 48]
    try:
        result = calculate_mean(sample_values)
        print(result)
    except ValueError as e:
        print(e)