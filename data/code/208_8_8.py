def calculate_numeric_mean(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("All elements in the list must be integers or floats.")
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [10, 25.5, 30, 4.5]
    mean_value = calculate_numeric_mean(sample_data)
    print(mean_value)