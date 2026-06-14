def calculate_numeric_mean(data):
    numeric_values = []
    for item in data:
        if isinstance(item, (int, float)):
            numeric_values.append(item)
    if not numeric_values:
        return None
    return sum(numeric_values) / len(numeric_values)
if __name__ == '__main__':
    sample_data = [10, "a", 25.5, None, 30, "hello", 4.5]
    mean_value = calculate_numeric_mean(sample_data)
    print(mean_value)