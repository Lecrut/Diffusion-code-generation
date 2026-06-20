def filter_and_average(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    if not positive_numbers:
        return 0.0
    return sum(positive_numbers) / len(positive_numbers)

if __name__ == '__main__':
    sample_data = [10, -20, 30, 40, -50]
    result = filter_and_average(sample_data)
    print(result)