def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 5.0, 6.7]
    average = calculate_average(sample_numbers)
    print(average)