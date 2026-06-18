def get_first_letters(strings):
    """
    Returns a list containing the first letter of each input string.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A list where each element is the first character 
                   corresponding to the respective input string.
                   
    Raises:
        ValueError: If any string in the list is empty or None.
    """
    result = []
    
    for s in strings:
        if not isinstance(s, str) or len(s) == 0:
            raise ValueError(f"Empty or invalid input found: {s!r}")
        
        # Efficiently access the first character using indexing
        result.append(s[0])
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, etc.)
    sample_strings = ["Python", "Scripting", "Robust", "Code"]

    try:
        first_letters = get_first_letters(sample_strings)
        
        # Print the results separated by spaces for clarity
        print(" ".join(first_letters))
        
    except ValueError as e:
        # Handle potential errors gracefully during execution of sample data
        print(f"Error processing input: {e}")