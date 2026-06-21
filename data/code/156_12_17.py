def calculate_average(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")
    if len(numbers) == 0:
        return 0
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_numbers = [2, 4, 6, 8, 10]
    avg = calculate_average(sample_numbers)
    print(avg)