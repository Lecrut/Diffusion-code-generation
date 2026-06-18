def total_string_length(string_list):
    """
    Calculates the combined length of all strings in a list efficiently.
    
    This function iterates through the provided list, calculating the len() 
    of each string and accumulating the sum. It avoids unnecessary type checks
    or conversions unless specifically needed for robustness against non-string inputs,
    though per requirements we assume valid input based on task description.

    Args:
        string_list (list[str]): A list containing strings.
        
    Returns:
        int: The total combined length of all strings in the list.
    """
    return sum(len(s) for s in string_list if isinstance(s, str))

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    sample_data = ["Hello", "World", "!"]
    
    result = total_string_length(sample_data)
    print(f"Total combined length: {result}")  # Expected output for the provided samples (5 + 5 + 1 = 11)