def calculate_mean(values):
    if not all(isinstance(v, float) for v in values):
        raise TypeError("All elements must be floats")
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(calculate_mean(sample_values))