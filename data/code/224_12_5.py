def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count > 0:
        average = total / count
    else:
        average = 0
    return average

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20]
    mean_value = calculate_mean(sample_values)
    print(mean_value)