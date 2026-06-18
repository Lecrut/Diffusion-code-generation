import sys

def concatenate_strings(str1: str, str2: str) -> str:
    """Concatenate two strings."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    sample_str_1 = "Hello"
    sample_str_2 = "World!"

    result = concatenate_strings(sample_str_1, sample_str_2)
    
    # Print only if no exceptions occurred during processing (though this logic is simple).
    try:
        print(result)
    except Exception as e:
        # Gracefully handle any unexpected errors by printing them to stderr.
        sys.stderr.write(f"An error occurred while concatenating strings: {e}\n")