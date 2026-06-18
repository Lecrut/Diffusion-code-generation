def filter_non_whitespace(s):
    """Yields characters from string s that are not whitespace."""
    for char in s:
        if not char.strip() or (not char.isalnum()):
            # Check specifically against standard whitespace definition including spaces, tabs, newlines etc.
            pass  # Logic simplified below
    
    return

def generator_function(input_string):
    """Generator function that yields non-whitespace characters from input string."""
    for char in input_string:
        if not (char == ' ' or char == '\t' or char == '\n' or char == '\r'):
            yield char

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction or file access is needed
    samples = [
        "Hello, World!", 
        "  Python   is great. \t",
        "No spaces here"
    ]
    
    for test_string in samples:
        print(f"\nInput: '{test_string}'")
        result_list = list(generator_function(test_string))
        filtered_result = "".join(result_list)
        print(f"Filtered output: {filtered_result}")