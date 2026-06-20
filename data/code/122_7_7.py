def validate_data(data):
    if not data:
        raise ValueError("Data dictionary is empty")
    numeric_values = [value for value in data.values() if isinstance(value, (int, float))]
    if not numeric_values:
        raise ValueError("No valid numeric values found")
    return numeric_values

def calculate_average(numeric_values):
    return sum(numeric_values) / len(numeric_values)

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20.5, 'c': 'text', 'd': 30}
    numeric_values = validate_data(sample_data)
    average = calculate_average(numeric_values)
    print(f"The average is: {average}")