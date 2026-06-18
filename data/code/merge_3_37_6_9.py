def append_strings(first: str, second: str) -> str:
    """Appends the second string to the first using an f-string."""
    return f"{first}{second}"

if __name__ == '__main__':
    sample_first = "Hello"
    sample_second = " World"
    result = append_strings(sample_first, sample_second)
    print(result)