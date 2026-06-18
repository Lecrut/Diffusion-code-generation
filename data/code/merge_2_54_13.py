import math
def find_midpoint_index(data):
    try:
        length = len(data)
        if length < 0:
            raise ValueError("Length of data structure cannot be negative.")
        midpoint = math.floor(length / 2)
        return int(midpoint)
    except TypeError as e:
        if "object" in str(e):
            raise ValueError("Input data must be a numeric-indexed structure (list, tuple, range).") from None
        else:
            raise TypeError(f"Invalid type for midpoint calculation. {e}")
if __name__ == '__main__':
    test_cases = [
        ([10, 20, 30], "Standard odd length list"),
        ([5, 6], "Even length list"),
        (range(7), "Range object"),
        ([] , "Empty list"),
        ("abc", "String as sequence"),
    ]
    for data, description in test_cases:
        try:
            result = find_midpoint_index(data)
            print(f"{description}: {result}")
        except (ValueError, TypeError) as e:
            print(f"{description} -> Error: {e}")