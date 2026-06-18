import string

def is_palindrome_two_pointers(s: str) -> bool:
    """
    Determines if a given string is a palindrome using a two-pointer approach.
    
    This method iterates from both ends of the filtered string (containing only alphanumeric characters),
    moving inward and comparing characters until they meet or cross, ignoring case sensitivity.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase for comparison
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    
    left, right = 0, len(filtered_chars) - 1
    
    while left < right:
        if filtered_chars[left] != filtered_chars[right]:
            return False
        left += 1
        right -= 1
        
    return True

def is_palindrome_slicing(s: str) -> bool:
    """
    Determines if a given string is a palindrome using string slicing.

    This method filters the input to create a clean version of the string, then checks
    for equality between the cleaned string and its reverse.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Create a list comprehension equivalent by filtering and converting characters
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    
    return "".join(filtered_chars) == "".join(reversed(filtered_chars))

if __name__ == '__main__':
    # Hard-coded sample values to test both implementations without user input
    samples = [
        "A man, a plan, a canal: Panama",
        "race car",
        "hello world!",
        "12321",
        "Not a palindrome",
        ""
    ]

    for sample in samples:
        result_tp = is_palindrome_two_pointers(sample)
        result_sl = is_palindrome_slicing(sample)
        
        print(f"Input: '{sample}'")
        print(f"Two-pointer method result: {result_tp}")
        print(f"Slicing method result: {result_sl}")
        if not (result_tp == result_sl):
            raise AssertionError("Results from both methods do not match.")
        print("-" * 40)