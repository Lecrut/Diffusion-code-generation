import statistics

def calculate_mean(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7, 5.0]
    try:
        print(calculate_mean(sample_values))
    except ValueError as e:
        print(e)