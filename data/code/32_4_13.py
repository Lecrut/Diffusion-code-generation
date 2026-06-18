"""
Module to calculate the total combined length of a list of strings efficiently.
This function avoids unnecessary conversions by iterating directly over characters,
making it O(n) where n is the total number of characters across all input strings.
"""

def calculate_total_length(string_list):
    """
    Calculates and returns the sum of lengths of all strings in the provided list.

    Args:
        string_list (list[str]): A list containing zero or more string objects.

    Returns:
        int: The total combined length of all strings in the list.
    
    Performance Note:
        This implementation iterates directly over characters using a generator expression,
        which is efficient for large lists and avoids intermediate data structures like sets 
        that might be created by methods like set().union() or similar overhead mechanisms.
    """
    return sum(len(s) for s in string_list)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, CLI args, network access, or file dependencies are needed.
    sample_data = ["hello", "world", "", "python"]
    
    result = calculate_total_length(sample_data)
    
    print(f"Total combined length: {result}")  # Expected output: 14 (5 + 5 + 0 + 6)