import statistics

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.0]
    try:
        print(calculate_mean(sample_values))
    except ValueError as e:
        print(e)