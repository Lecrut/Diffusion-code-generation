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
    sample_data = "10 5 22 8 15 3"
    filename = "sample_numbers.txt"
    with open(filename, 'w') as f:
        f.write(sample_data)
    minimum, maximum = find_min_max(filename)
    if minimum is not None and maximum is not None:
        print(f"Minimum value: {minimum}")
        print(f"Maximum value: {maximum}")
    else:
        print("Error processing file or no data found.")