def append_strings(first: str, second: str) -> str:
    """Returns a new string formed by appending 'second' to 'first'."""
    return f"{first}{second}"

if __name__ == '__main__':
    sample_first = "Hello"
    sample_second = ", World!"
    result = append_strings(sample_first, sample_second)
    print(result)