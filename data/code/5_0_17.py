def calculate_length_difference(length1, length2):
    if not isinstance(length1, (int, float)):
        raise TypeError(f"length1 must be a number, got {type(length1).__name__}")
    if not isinstance(length2, (int, float)):
        raise TypeError(f"length2 must be a number, got {type(length2).__name__}")
    if length1 < 0 or length2 < 0:
        raise ValueError("Lengths cannot be negative")
    return abs(length1 - length2)

if __name__ == '__main__':
    result = calculate_length_difference(10.5, 5.3)
    print(result)