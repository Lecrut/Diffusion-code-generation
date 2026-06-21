def split_string_by_whitespace(text):
    return text.split()

if __name__ == '__main__':
    samples = {
        "Hello world": ["Hello", "world"],
        "  This   has\tmultiple\nspaces ": ["This", "has", "multiple", "spaces"],
        "NoSpacesHere": ["NoSpacesHere"],
        "a\t\nb\r\n c": ["a", "b", "c"]
    }

    for sample, expected in samples.items():
        result = split_string_by_whitespace(sample)
        print(f"Input: '{sample}'")
        print(f"Expected Output: {expected}")
        print(f"Actual Output: {result}")
        print()