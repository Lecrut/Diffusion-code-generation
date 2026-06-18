def append_strings(str1: str, str2: str) -> str:
    """Appends the second string to the first using an f-string."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    sample_first = "Hello"
    sample_second = " World!"
    result = append_strings(sample_first, sample_second)
    print(result)