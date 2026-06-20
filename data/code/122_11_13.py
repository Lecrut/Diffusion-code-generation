def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (15, 25, 35, 45)
    average = calculate_average(sample_values)
    print(average)