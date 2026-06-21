import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [12, 24, 36, 48, 60]
    average_value = calculate_average(sample_numbers)
    print(average_value)