def process_string(s: str) -> tuple[str, str, str]:
    """Returns a tuple with (original_lowercase_reversed_case)."""
    original = s
    lowercased = s.lower()
    reversed_lowered = ''.join(reversed(lowercased))
    return (original, lowercased, reversed_lowered)

if __name__ == '__main__':
    sample_input = "Hello World"
    result = process_string(sample_input)
    print(result[0])  # Original: Hello World
    print(result[1])  # Lowercase: hello world
    print(result[2])  # Reversed case: dlrow olleh