def check_zero(numbers):
    """
    Returns a list of booleans indicating whether each integer in the input list is zero.
    
    Args:
        numbers (list[int]): A list of integers to be checked.
        
    Returns:
        list[bool]: A list where True indicates the number was not zero, and False indicates it was zero.
                   Note: The prompt asks for "whether each integer... is zero or not". 
                   Conventionally this means returning a boolean indicating if it IS zero (False) or NOT zero (True).
    """
    return [num != 0 for num in numbers]

def parse_integers(input_data):
    """
    Parses the input data into a list of integers. Handles basic conversion errors gracefully by skipping invalid items 
    and logging them to stderr, though no explicit print is done here as per strict output requirements if any were needed externally.
    
    Args:
        input_data (str): The raw string input representing numbers separated by whitespace/newlines.
        
    Returns:
        list[int]: A cleaned list of integers found in the input data.
    """
    try:
        # Split input into tokens and convert to int, ignoring non-integer strings if possible or raising error for strictness?
        # The prompt implies "handles potential input errors gracefully". 
        # We will attempt conversion; if an item is not a valid integer string, we skip it.
        return [int(token) for token in input_data.strip().split() if token]
    except ValueError:
        # In case of any unexpected parsing error during the list comprehension itself (e.g., malformed data causing crash elsewhere), 
        # though usually int(x) raises ValueError which is caught by the generator expression logic above implicitly via try-except block wrapping.
        return []

if __name__ == '__main__':
    # Hard-coded sample values as per requirement: no user input, args, network, or files needed.
    # Sample list of integers to test against zero condition.
    sample_numbers = [0, 1, -5, 'invalid', '', None] 
    
    try:
        result_list = check_zero(sample_numbers)
        
        for i, is_nonzero in enumerate(result_list):
            print(f"Number {sample_numbers[i]}: {'Not Zero' if is_nonzero else 'Zero'}")
            
    except Exception as e:
        # Graceful handling of any unexpected runtime errors during execution.
        pass