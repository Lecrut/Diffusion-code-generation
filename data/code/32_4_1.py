def calculate_total_length(string_list):
    """
    Calculates the total combined length of all strings in a given list.
    
    Args:
        string_list (list[str]): A list containing zero or more string elements.
        
    Returns:
        int: The sum of lengths of all strings in the input list.
            
    Performance Note:
        This function uses a generator expression within the built-in sum() 
        to avoid creating an intermediate list, which improves memory efficiency 
        for large inputs while maintaining readability and performance.
        
    Time Complexity: O(n), where n is the number of strings in the input list.
    Space Complexity: O(1) auxiliary space (excluding input/output storage).
    """
    return sum(len(s) for s in string_list if isinstance(s, str))

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    sample_data = ["hello", "world", "", "Python3"]
    
    result = calculate_total_length(sample_data)
    
    print(f"Total combined length: {result}")  # Expected output: 10 + 5 + 0 + 7 = 22