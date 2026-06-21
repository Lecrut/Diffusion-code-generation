def validate_data(data):
    if not data:
        raise ValueError("The input list cannot be empty")

def calculate_mean(values):
    validate_data(values)
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [10, 20.5, 30, 40.75]
    mean_value = calculate_mean(sample_values)
    print(mean_value)