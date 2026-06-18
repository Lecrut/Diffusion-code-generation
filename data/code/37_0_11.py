def combine_strings(s1: str, s2: str) -> str:
    """Concatenates two input strings into a single string."""
    return f"{s1}{s2}"

if __name__ == '__main__':
    result = combine_strings("Hello", "World")
    print(result)