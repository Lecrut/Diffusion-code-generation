def validate_input(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("Input must be a tuple of numeric values")

def cumulative_sum(numbers):
    return tuple(sum(numbers[:i+1]) for i in range(len(numbers)))

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    validate_input(sample_values)
    print(cumulative_sum(sample_values))