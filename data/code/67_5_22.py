def add_numbers(a, b):
    try:
        result = float(a) + float(b)
        return result
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be numbers")

if __name__ == '__main__':
    sample_values = [(5, 10), ('3.5', '2.5'), ('a', 5)]
    for a, b in sample_values:
        try:
            print(add_numbers(a, b))
        except ValueError as e:
            print(e)