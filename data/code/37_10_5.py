def combine_strings(str1: str, str2: str) -> str:
    """Combines two input strings into a single string separated by a space."""
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user interaction.
    sample_str_1 = "Hello"
    sample_str_2 = "World"

    result_string = combine_strings(sample_str_1, sample_str_2)
    
    print(result_string)