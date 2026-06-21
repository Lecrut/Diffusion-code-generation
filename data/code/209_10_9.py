import statistics

def validate_input(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    for value in values:
        if not isinstance(value, (int, float)):
            raise TypeError("All elements must be numbers")

def calculate_mean(values):
    validate_input(values)
    return statistics.mean(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        mean_value = calculate_mean(sample_values)
        print(f"The arithmetic mean is: {mean_value}")
    except ValueError as e:
        print(e)