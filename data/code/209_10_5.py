import statistics

def calculate_mean(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        mean_value = calculate_mean(sample_values)
        print(mean_value)
    except ValueError as e:
        print(e)