import os
def find_min_max(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")
    with open(filename, 'r') as file:
        data = file.read().split()
        if not data:
            return None, None
        numbers = [int(x) for x in data]
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum
if __name__ == '__main__':
    sample_filename = "numbers.txt"
    sample_data = "10 5 22 8 30 1"
    with open(sample_filename, 'w') as f:
        f.write(sample_data)
    min_val, max_val = find_min_max(sample_filename)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")