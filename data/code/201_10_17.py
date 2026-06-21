import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [12, 18, 24, 30, 36]
    average_value = calculate_average(sample_values)
    print(average_value)