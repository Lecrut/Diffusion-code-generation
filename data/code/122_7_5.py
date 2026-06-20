def calculate_average(data):
    numeric_values = [v for v in data.values() if isinstance(v, (int, float))]
    if not numeric_values:
        raise ValueError("No valid numeric values found")
    return sum(numeric_values) / len(numeric_values)

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20.5, 'c': 'text', 'd': 30}
    try:
        avg = calculate_average(sample_dict)
        print(f"The average is: {avg}")
    except ValueError as e:
        print(e)