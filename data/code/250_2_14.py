def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4, 5)
    print(f"The average of {sample_values} is: {calculate_average(sample_values)}")