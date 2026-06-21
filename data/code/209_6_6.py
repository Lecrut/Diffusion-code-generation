def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [12, 24, 36]
    average = calculate_average(sample_numbers)
    print(average)