import sys

def concatenate_strings(str1: str, str2: str) -> str:
    """Concatenate two strings without side effects."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    sample_str_1 = "Hello"
    sample_str_2 = "World"

    result = concatenate_strings(sample_str_1, sample_str_2)
    
    # Print only if a valid concatenation was performed (handles empty strings gracefully).
    print(result)