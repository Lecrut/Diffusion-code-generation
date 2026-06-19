reverse_string = lambda s: ''.join(reversed(s))

if __name__ == '__main__':
    sample_strings = {"short": "hello", "long": "this is a test string for optimization" * 100}
    reversed_samples = {key: reverse_string(value) for key, value in sample_strings.items()}
    for key, value in reversed_samples.items():
        print(f"Original ({key}): {sample_strings[key]}, Reversed: {value[:50]}...")