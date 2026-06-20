def calculate_average(data):
    numeric_values = [value for value in data.values() if isinstance(value, (int, float))]
    if not numeric_values:
        raise ValueError("No valid numbers found")
    return sum(numeric_values) / len(numeric_values)

if __name__ == '__main__':
    sample_dict = {'x': 50, 'y': 25.5, 'z': 'data', 'w': 75}
    try:
        avg = calculate_average(sample_dict)
        print(f"The average is: {avg}")
    except ValueError as e:
        print(e)