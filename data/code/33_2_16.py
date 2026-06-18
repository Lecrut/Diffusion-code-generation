import sys

def strip_all_spaces(input_string: str) -> str:
    """
    Removes all spaces (both internal and external) from the input string.
    
    Args:
        input_string (str): The multi-line string to process.
        
    Returns:
        str: A new string with no whitespace characters remaining.
    """
    return "".join(input_string.split())

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, ensuring no user input or file I/O dependencies.
    # This block is self-contained and runs without network access or pre-existing files.
    
    raw_data = (
        "   Hello World  \n"
        "This has multiple spaces in the middle.\n\n\tAnd another line with tabs."
    )

    result_string: str = strip_all_spaces(raw_data)

    # Output using standard output file handle for best practices, though simple print is sufficient.
    sys.stdout.write(result_string + '\n')