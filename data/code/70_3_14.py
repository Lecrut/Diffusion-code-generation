def boundary_numbers(input_string):
    parts = input_string.split()
    if not parts:
        raise ValueError("Input string contains no numbers")
    values = [int(part) for part in parts]
    if not values:
        raise ValueError("Parsed list is empty")
    return values[0], values[-1]

if __name__ == '__main__':
    raw_data = "100 200 300 400 500"
    start, end = boundary_numbers(raw_data)
    print(start, end)