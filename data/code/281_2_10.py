def validate_input(values):
    if not isinstance(values, list) or len(values) != 5:
        raise ValueError("Input must be a list of exactly five integers")

def calculate_sum(values):
    total = 0
    for value in values:
        total += value
    return total

if __name__ == '__main__':
    sample_values = [10, 25, 30, 45, 5]
    validate_input(sample_values)
    result = calculate_sum(sample_values)
    print(result)