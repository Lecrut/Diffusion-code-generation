def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = (3, 5, 7, 9)
    print(calculate_average(sample_numbers))