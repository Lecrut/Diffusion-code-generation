def calculate_mean(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(f"Average of {sample_values}: {calculate_mean(sample_values)}")