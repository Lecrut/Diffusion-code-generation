def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 6, 5]
    average = calculate_average(sample_numbers)
    print(average)