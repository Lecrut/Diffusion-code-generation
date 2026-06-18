def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    test_cases = [
        ("Hello World", 5),
        ("Python", 0),
        ("ABCDEF", 3),
        ("a", 0),
        ("test string", 8)
    ]
    for input_str, idx in test_cases:
        result = delete_char_at_index(input_str, idx)
        expected = input_str[:idx] + input_str[idx+1:]
        assert result == expected, f"Test failed for '{input_str}' at index {idx}. Got '{result}', expected '{expected}'"
    print("All unit tests passed.")