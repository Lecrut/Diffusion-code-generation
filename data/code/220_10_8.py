import statistics

def mean_of_numbers(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    try:
        print(mean_of_numbers(sample_values))
    except ValueError as e:
        print(e)