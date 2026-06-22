def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = calculate_average(sample_list)
    print(result)