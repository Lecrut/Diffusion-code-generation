def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    sample_strings = {
        "apple": "elppa",
        "banana": "ananab",
        "cherry": "yrrehc"
    }
    for original, expected in sample_strings.items():
        result = reverse_string(original)
        print(f"Original: {original}, Reversed: {result}, Expected: {expected}")