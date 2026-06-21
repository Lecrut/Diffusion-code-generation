import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 25, 32, 48, 15]
    avg_value = calculate_average(sample_numbers)
    print(avg_value)