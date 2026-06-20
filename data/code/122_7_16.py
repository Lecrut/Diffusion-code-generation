def average_values(data):
    numeric_values = [value for value in data.values() if isinstance(value, (int, float))]
    if not numeric_values:
        raise ValueError("No valid numbers found")
    return sum(numeric_values) / len(numeric_values)

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20.5, 'c': 'text', 'd': 30}
    try:
        avg = average_values(sample_data)
        print(f"The average is: {avg}")
    except ValueError as e:
        print(e)