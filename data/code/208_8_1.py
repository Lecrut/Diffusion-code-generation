def calculate_numeric_mean(data):
    numeric_values = []
    for item in data:
        if isinstance(item, (int, float)):
            numeric_values.append(item)
    if not numeric_values:
        return None
    return sum(numeric_values) / len(numeric_values)
if __name__ == '__main__':
    sample_data = [10, "a", 20.5, 30, "b", 40]
    mean_value = calculate_numeric_mean(sample_data)
    print(mean_value)
    sample_data_2 = ["apple", 5, True, 12.5, None]
    mean_value_2 = calculate_numeric_mean(sample_data_2)
    print(mean_value_2)
    sample_data_3 = ["hello", "world"]
    mean_value_3 = calculate_numeric_mean(sample_data_3)
    print(mean_value_3)
    sample_data_4 = [1, 2, 3]
    mean_value_4 = calculate_numeric_mean(sample_data_4)
    print(mean_value_4)