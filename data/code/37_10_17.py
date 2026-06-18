def combine_strings(str1: str, str2: str) -> str:
    """Combines two input strings into a single string separated by a space."""
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    sample_input_1 = "Hello"
    sample_input_2 = "World"

    result = combine_strings(sample_input_1, sample_input_2)
    
    print(result)