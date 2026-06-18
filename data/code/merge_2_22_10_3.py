def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
    return s
if __name__ == '__main__':
    test_cases = [
        ("Hello World", 5),
        ("Python", -2),
        ("Test", 10),
        ("A", 0)
    ]
    for text, idx in test_cases:
        try:
            result = delete_char_at_index(text, idx)
            print(f"Input: '{text}', Index: {idx} -> Output: '{result}'")
        except Exception as e:
            print(f"Error with Input: '{text}', Index: {idx}: {e}")