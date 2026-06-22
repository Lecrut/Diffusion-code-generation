def calculate_length_difference(length1, length2):
    if not isinstance(length1, (int, float)):
        raise ValueError(f"Invalid length: {length1}")
    if not isinstance(length2, (int, float)):
        raise ValueError(f"Invalid length: {length2}")
    if length1 < 0 or length2 < 0:
        raise ValueError("Lengths cannot be negative")
    return abs(length1 - length2)

if __name__ == '__main__':
    result = calculate_length_difference(10.5, 4.2)
    print(result)