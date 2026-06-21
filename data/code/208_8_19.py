def calculate_numeric_mean(data):
    numeric_values = [item for item in data if isinstance(item, (int, float))]
    return sum(numeric_values) / len(numeric_values) if numeric_values else None

if __name__ == '__main__':
    sample_data = [10, "a", 25.5, None, 30, "hello", 4.5]
    mean_value = calculate_numeric_mean(sample_data)
    print(mean_value)