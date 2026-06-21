import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    try:
        return statistics.mean(numbers)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    sample_numbers = [10, 25, 32, 48, 15]
    result = calculate_average(sample_numbers)
    print(result)