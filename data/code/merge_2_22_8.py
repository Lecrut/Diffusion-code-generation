def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(s):
        raise IndexError(f"Index {index} is out of bounds for string of length {len(s)}")
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    test_cases = [
        ("hello", 0, "ello"),
        ("world", 4, "worl"),
        ("python", 5, "pytho"),
        ("a", 0, ""),
        ("abcde", 2, "abde"),
        ("test", -1, IndexError),
    ]
    for s, idx, expected in test_cases:
        try:
            result = delete_char_at_index(s, idx)
            if isinstance(expected, type):
                assert isinstance(result, expected), f"Expected {expected.__name__}, got {type(result)}"
            else:
                assert result == expected, f"For input '{s}' at index {idx}: expected '{expected}', got '{result}'"
        except Exception as e:
            if not (isinstance(expected, type) and isinstance(e, expected)):
                raise AssertionError(f"Test failed for '{s}' at {idx}. Expected exception {expected.__name__}, but raised {type(e).__name__}: {e}")
    print("All tests passed.")