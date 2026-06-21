def calculate_mean(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    calculated_mean = calculate_mean(sample_values)
    print(f"The mean of {sample_values} is: {calculated_mean}")