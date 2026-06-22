import statistics

def compute_mean(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    try:
        mean_value = compute_mean(sample_values)
        print(f"The arithmetic mean is: {mean_value}")
    except ValueError as e:
        print(e)