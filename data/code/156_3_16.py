def calculate_mean(values):
    if not isinstance(values, list) or len(values) == 0:
        raise ValueError("Input must be a non-empty list of floats")
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(calculate_mean(sample_values))