def calculate_range(values):
    return max(values) - min(values)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(calculate_range(sample_values))