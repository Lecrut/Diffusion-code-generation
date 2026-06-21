def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0.0
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    result = calculate_mean(sample_values)
    print(f"Mean of {sample_values}: {result}")