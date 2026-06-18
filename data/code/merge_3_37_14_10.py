import sys

def concatenate_strings(str1: str, str2: str) -> str:
    """
    Concatenates two input strings into a single string.
    
    Args:
        str1 (str): The first string operand.
        str2 (str): The second string operand.
        
    Returns:
        str: The concatenated result of str1 + str2.
    """
    return f"{str1}{str2}"

def main():
    # Hard-coded sample values to ensure the script runs without user input,
    # command-line arguments, network access, or pre-existing files.
    sample_str_1 = "Hello"
    sample_str_2 = "World"

    result = concatenate_strings(sample_str_1, sample_str_2)

    print(result)

if __name__ == '__main__':
    main()