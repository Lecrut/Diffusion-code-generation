import statistics

def calculate_mean(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    return statistics.mean(values)

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    try:
        mean_value = calculate_mean(sample_values)
        print(f"The arithmetic mean is: {mean_value}")
    except ValueError as e:
        print(e)