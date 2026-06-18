def delete_char(s: str, index: int) -> str:
    if not isinstance(index, int):
        return s
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        return s
if __name__ == '__main__':
    test_cases = [
        ("Hello World", 0),
        ("Python3.9", -5),
        ("ABC", 2),
        ("Test String!", 10)
    ]
    for string, idx in test_cases:
        result = delete_char(string, idx)
        print(f"Input: '{string}', Index: {idx} -> Output: '{result}'")