def calculate_numeric_mean(data):
    numeric_values = [item for item in data if isinstance(item, (int, float))]
    return sum(numeric_values) / len(numeric_values) if numeric_values else None

if __name__ == '__main__':
    sample_data1 = [10, "a", 25.5, None, 30, "hello", 4.5]
    print(calculate_numeric_mean(sample_data1))
    sample_data2 = ["apple", 5, True, 12.5, None]
    print(calculate_numeric_mean(sample_data2))
    sample_data3 = ["hello", "world"]
    print(calculate_numeric_mean(sample_data3))