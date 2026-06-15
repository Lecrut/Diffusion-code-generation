import os
def find_min_max(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    with open(filename, 'r') as file:
        data = []
        for line in file:
            try:
                data.append(float(line.strip()))
            except ValueError:
                continue
    if not data:
        return None, None
    minimum = min(data)
    maximum = max(data)
    return minimum, maximum
if __name__ == '__main__':
    sample_filename = "numbers.txt"
    with open(sample_filename, 'w') as f:
        f.write("10\n")
        f.write("5\n")
        f.write("22\n")
        f.write("-3\n")
        f.write("45\n")
    min_val, max_val = find_min_max(sample_filename)
    if min_val is not None and max_val is not None:
        print(f"Minimum value: {min_val}")
        print(f"Maximum value: {max_val}")
    else:
        print("No valid numbers found in the file.")