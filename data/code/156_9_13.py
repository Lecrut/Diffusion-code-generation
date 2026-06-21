def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return 0
    try:
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        return average
    except TypeError:
        return 0

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(f"Average of {sample_data}: {calculate_average(sample_data)}")