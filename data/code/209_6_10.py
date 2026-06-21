def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [12, 24, 36]
    average = calculate_average(sample_values)
    print(average)