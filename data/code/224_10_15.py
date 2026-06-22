def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    print(f"Mean of {sample_values}: {calculate_mean(sample_values)}")