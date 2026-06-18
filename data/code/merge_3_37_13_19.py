def join_strings(str1: str, str2: str) -> str:
    """Join two strings using an f-string."""
    return f"{str1} {str2}"

if __name__ == '__main__':
    sample_1 = "Hello"
    sample_2 = "World!"
    result = join_strings(sample_1, sample_2)
    print(result)