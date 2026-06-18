def combine_strings(str1: str, str2: str) -> str:
    """Returns the concatenation of two input strings."""
    return str1 + str2

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "World"
    result = combine_strings(sample_str1, sample_str2)
    print(result)