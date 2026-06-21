def calculate_average(numbers):
    if not isinstance(numbers, list) or not numbers:
        return None
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        return None

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(f"Average of {sample_values}: {calculate_average(sample_values)}")