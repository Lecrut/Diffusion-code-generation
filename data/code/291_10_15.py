def compare_lengths(length1: float, length2: float) -> float:
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return max(length1, length2)

if __name__ == '__main__':
    length_a = 5.5
    length_b = 3.2
    try:
        longer_length = compare_lengths(length_a, length_b)
        print(f"The longer length is: {longer_length} meters")
    except ValueError as e:
        print(f"An error occurred: {e}")