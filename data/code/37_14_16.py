import sys

def concatenate_strings(str1: str, str2: str) -> str:
    """Concatenates two strings without any side effects."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    SAMPLE_STR_1 = "Hello"
    SAMPLE_STR_2 = "World"

    result: str = concatenate_strings(SAMPLE_STR_1, SAMPLE_STR_2)
    
    # Print the concatenated string directly using f-string formatting for clarity and performance.
    print(result)