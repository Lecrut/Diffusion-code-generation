def find_occurrences(text: str, substring: str) -> list[tuple[int, int]]:
    """
    Finds all starting indices of a specific substring within a larger text.
    
    Args:
        text (str): The main string to search in.
        substring (str): The target substring to find.
        
    Returns:
        List of tuples where each tuple is (start_index, end_index).
        If not found, returns an empty list.
    """
    # Handle edge cases for substring length and special characters
    if len(substring) <= 0 or text == "":
        return []

    occurrences = []
    
    current_idx = 0
    
    while True:
        # Find the next occurrence of substring in the remaining part of text
        idx = text.find(substring, current_idx)

if __name__ == '__main__':
    pass
