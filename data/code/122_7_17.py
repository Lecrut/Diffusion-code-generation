def average_of_values(data):
    numbers = [v for v in data.values() if isinstance(v, (int, float))]
    if not numbers:
        raise ValueError("No valid numeric values found")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20.5, 'c': 'not a number', 'd': 30}
    try:
        avg = average_of_values(sample_data)
        print(f"The average is: {avg}")
    except ValueError as e:
        print(e)