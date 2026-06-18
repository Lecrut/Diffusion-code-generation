import math
def find_midpoint_index(data):
    try:
        length = len(data)
        if length < 1:
            raise ValueError("Input data must have a positive integer length.")
        midpoint_index = math.floor(length / 2)
        return int(midpoint_index)
    except TypeError as e:
        if "object of type" in str(e):
            raise TypeError("Input must be a list, tuple, range, or similar sequence.") from None
        else:
            raise
if __name__ == '__main__':
    test_cases = [
        ([10], "Single element"),
        ([-5], "Negative single element"),
        ([], "Empty list - should return None or handle gracefully based on logic above, currently raises ValueError"),
        ((-3.7,), "Float wrapped in tuple for length check simulation if needed, but len() works on tuples of floats too"),
        ("abc", "String input (sequence)"),
    ]
    for data, description in test_cases:
        try:
            result = find_midpoint_index(data)
            print(f"Input: {description} -> Data type hint: {type(data).__name__}, Result Index: {result}")
        except (ValueError, TypeError) as exc:
            error_type = "ValueError" if isinstance(exc, ValueError) else "TypeError"
            print(f"Input: {description} -> Error ({error_type}): {exc}")
    class NegativeLenSimulator:
        def __len__(self): return -5
    try:
        find_midpoint_index(NegativeLenSimulator())
    except ValueError as ve:
        print(f"Negative Length Simulation -> Caught expected error: {ve}")