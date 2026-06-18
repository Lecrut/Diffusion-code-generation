def combine_strings(str1: str, str2: str) -> str:
    """Combines two input strings separated by a space."""
    return f"{str1} {str2}"

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "World"
    result_string = combine_strings(sample_str1, sample_str2)
    print(result_string)