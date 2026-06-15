def analyze_data(filename):
    try:
        with open(filename, 'r') as file:
            data = [float(line.strip()) for line in file]
        if not data:
            return None, None, None
        minimum = min(data)
        maximum = max(data)
        data_range = maximum - minimum
        return minimum, maximum, data_range
    except FileNotFoundError:
        return None, None, None
    except ValueError:
        return None, None, None
if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("10\n")
        f.write("5\n")
        f.write("20\n")
        f.write("3\n")
        f.write("15\n")
    minimum_val, maximum_val, data_range = analyze_data(sample_filename)
    if minimum_val is not None:
        print(f"Minimum: {minimum_val}")
        print(f"Maximum: {maximum_val}")
        print(f"Range: {data_range}")