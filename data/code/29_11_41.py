def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    sample_strings = {
        "hello": "olleh",
        "world": "dlrow",
        "Python": "nohtyP"
    }
    for original in sample_strings:
        try:
            result = reverse_string(original)
            expected = sample_strings[original]
            print(f"Original: {original}, Reversed: {result}, Expected: {expected}")
        except ValueError as e:
            print(f"Error: {e}")