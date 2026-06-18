def combine_strings(str1: str, str2: str) -> str:
    """Concatenates two input strings into a single string."""
    return str1 + str2

if __name__ == '__main__':
    sample_str_1 = "Hello"
    sample_str_2 = "World"
    result = combine_strings(sample_str_1, sample_str_2)
    print(result)