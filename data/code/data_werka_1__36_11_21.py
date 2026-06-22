reverse_string = lambda s: ''.join(reversed(s))

if __name__ == '__main__':
    sample_strings = {"short": "hello", "long": "this is a test string for optimization" * 10}
    for key, value in sample_strings.items():
        reversed_value = reverse_string(value)
        print(f"Original ({key}): {value[:50]}..., Reversed: {reversed_value[:50]}...")