def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    sample_strings = {
        "hello": "olleh",
        "world": "dlrow",
        "python": "nohtyp"
    }
    for original, expected in sample_strings.items():
        result = reverse_string(original)
        print(f"Original: {original}, Reversed: {result}, Expected: {expected}")