import sys

def concatenate_strings(str1: str, str2: str) -> str:
    """
    Concatenates two input strings without side effects or external dependencies.
    
    Args:
        str1 (str): The first string operand.
        str2 (str): The second string operand.
        
    Returns:
        str: A new string containing the concatenation of both inputs.
    """
    return f"{str1}{str2}"

def main() -> None:
    # Hard-coded sample values as per requirements to avoid any user input, 
    # command-line arguments, or network access.
    sample_str_1 = "Hello"
    sample_str_2 = "World"

    result = concatenate_strings(sample_str_1, sample_str_2)
    
    # Print the concatenated string to standard output only once.
    print(result)

if __name__ == '__main__':
    main()