#!/usr/bin/env python3
"""Script to read a list of strings and print the first letter of each."""

def get_first_letter(string: str) -> str:
    """Return the first character of the given string if it is not empty, otherwise return an empty string.

    Args:
        string (str): The input string.

    Returns:
        str: A single-character string containing the first letter, or an empty string if the input is empty.
    """
    if not string:
        return ""
    return string[0]

def main():
    # Hard-coded sample list of strings as per task requirements (no user input required).
    sample_strings = [
        "Hello World",
        "",
        "Python",
        "Data Science",
        None  # Will be handled gracefully if passed, though not in our specific loop below.
    ]

    # Filter out non-string elements to ensure robustness for the expected task scope.
    valid_strings = [s for s in sample_strings if isinstance(s, str)]

    print("First letters of each string:")
    
    # Efficient and clear loop using enumerate or simple index iteration.
    for i in range(len(valid_strings)):
        current_str = valid_strings[i]
        first_char = get_first_letter(current_str)
        
        # Print result with the original input context if desired, otherwise just the char.
        print(f"String {i+1}: '{current_str}' -> First letter: '{first_char}'")

if __name__ == '__main__':
    main()