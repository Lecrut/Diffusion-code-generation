def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.8, 4.1, 5.0]
    average = calculate_average(sample_numbers)
    print(average)