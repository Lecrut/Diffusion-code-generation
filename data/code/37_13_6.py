def join_strings(str1: str, str2: str) -> str:
    """Joins two strings using an f-string."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = ", World!"
    result = join_strings(sample_str1, sample_str2)
    print(result)