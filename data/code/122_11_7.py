def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (5, 10, 15, 20)
    average = calculate_average(sample_values)
    print(average)