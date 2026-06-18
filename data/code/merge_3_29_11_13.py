def reverse_word(text: str) -> str:
    """Returns the reversed version of the input string using slicing."""
    return text[::-1]

if __name__ == '__main__':
    # Sample test cases running without user interaction or files
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "a"
    ]

    for sample in samples:
        result = reverse_word(sample)
        print(f'Input: "{sample}" -> Output: "{result}"')