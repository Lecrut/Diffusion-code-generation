def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
    if index < 0 or index >= len(s):
        raise ValueError(f"Index {index} is out of range for string of length {len(s)}.")
if __name__ == '__main__':
    test_cases = [
        ("Hello World", 5),
        ("Python", -1),
        ("Test String", 20),
        ("Single", 6)
    ]
    for string, idx in test_cases:
        try:
            result = delete_char_at_index(string, idx)
            print(f"Input: '{string}', Index: {idx} -> Output: '{result}'")
        except (ValueError, TypeError) as e:
            print(f"Input: '{string}', Index: {idx} -> Error: {e}")