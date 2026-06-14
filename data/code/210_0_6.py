def find_min_max(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
            if not data:
                return None, None
            numbers = [float(x) for x in data]
            if not numbers:
                return None, None
            minimum = min(numbers)
            maximum = max(numbers)
            return minimum, maximum
    except FileNotFoundError:
        return None, None
    except ValueError:
        return None, None
if __name__ == '__main__':
    sample_data = "10 5 22 8 30 1"
    filename = "sample_numbers.txt"
    with open(filename, 'w') as f:
        f.write(sample_data)
    minimum_val, maximum_val = find_min_max(filename)
    if minimum_val is not None and maximum_val is not None:
        print(f"Minimum value: {minimum_val}")
        print(f"Maximum value: {maximum_val}")
    else:
        print("Error reading or processing the file.")