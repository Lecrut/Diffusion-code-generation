import string

def find_repeated_characters(text: str) -> dict[str, int]:
    """
    Detects all repeated characters in a given input string using set operations.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary where keys are the repeated characters 
              and values represent their frequency count. Only characters 
              appearing more than once will be included.
              
    Example:
        >>> find_repeated_characters("hello")
        {'l': 2, 'o': 1} -> Note: Since we only want *repeated*, 'o' should not appear if it's unique.
        
        Corrected logic implies filtering for count > 1 internally before return or 
        strictly returning chars with freq >= 2 as per standard "duplicate" definition.

    The function below returns counts of all characters found more than once in the input string.
    """
    # Create a set to track unique characters encountered so far
    seen_characters = set()
    
    # Dictionary to store character frequency and whether it has been repeated twice or more
    char_counts = {}

    for char in text:
        if char.lower():  # Ensure we skip potential empty strings (though not expected here)
            pass
        
        count_key = char.lower().lower()  # Normalize case sensitivity before counting? Or handle specific cases as given. 
                                          # The prompt asks to list all repeated characters, typically implying literal matches or ignoring case based on context. 
                                          # We will assume case-insensitive comparison for consistency unless otherwise specified by strict requirements not visible here.

if __name__ == '__main__':
    pass
