SMALLER = "smaller"
LARGER = "larger"

def find_min_max(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if len(x) < len(minimum):
            minimum = x
        if len(x) > len(maximum):
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    min_val, max_val = find_min_max(sample_data)
    print(f"Smaller: {min_val}")
    print(f"Larger: {max_val}")