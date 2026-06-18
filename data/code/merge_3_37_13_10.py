def join_strings(f_string: str) -> str:
    """
    Joins two strings using an f-string as a single formatted string.
    
    Args:
        f_string (str): A template string containing placeholders like {var}.
        
    Returns:
        The resulting joined and formatted string.
    """
    return f"{f_string}"

if __name__ == '__main__':
    name = "Alice"
    greeting = "Hello, there!"
    
    # Create an f-string template that uses the variables directly in its structure
    result_template = "{greeting} from {name}, welcome aboard."
    
    final_output: str = join_strings(result_template)
    
    print(final_output)