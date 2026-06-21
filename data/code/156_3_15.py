def is_valid_list_of_floats(values):
    return isinstance(values, list) and all(isinstance(x, float) for x in values) and len(values) > 0

def calculate_mean(numbers):
    if not is_valid_list_of_floats(numbers):
        raise ValueError("Input must be a non-empty list of floats")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(calculate_mean(sample_values))