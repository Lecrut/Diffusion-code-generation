def append_strings(str1: str, str2: str) -> str:
    """Returns a new string formed by appending str2 to str1."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = " World!"
    result = append_strings(sample_str1, sample_str2)
    print(result)