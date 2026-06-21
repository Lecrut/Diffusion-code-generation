def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20, 25]
    average = calculate_average(sample_values)
    print(average)