import statistics

def compute_mean(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 5.0]
    try:
        result = compute_mean(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)