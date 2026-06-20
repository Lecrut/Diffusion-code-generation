import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    try:
        return statistics.mean(numbers)
    except TypeError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_average(sample_values))
    print(calculate_average([]))