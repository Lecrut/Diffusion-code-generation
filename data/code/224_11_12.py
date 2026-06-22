def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    average = calculate_average(sample_values)
    print(average)