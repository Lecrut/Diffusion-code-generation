import string

def is_palindrome_two_pointers(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer approach.
    
    This method ignores case, spaces, and punctuation by creating a cleaned 
    version of the string consisting only of alphanumeric characters. Then it 
    uses pointers to traverse from both ends towards the center comparing characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Time Complexity: O(n) where n is the length of the cleaned substring.
    Space Complexity: O(1) excluding the space for cleaning the string.
    """
    # Create a list to store only alphanumeric characters in lowercase
    valid_chars = [c.lower() for c in s if c.isalnum()]

    left, right = 0, len(valid_chars) - 1

    while left < right:
        if not (valid_chars[left] == valid_chars[right]):
            return False
        left += 1
        right -= 1

    return True

def is_palindrome_slicing(s: str) -> bool:
    """
    Check if a string is a palindrome using two separate string passes.
    
    This method first cleans the input string to remove non-alphanumeric 
    characters and convert to lowercase, similar to the two-pointer approach.
    Then it checks for equality between the cleaned string and its reverse.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time Complexity: O(n) where n is the length of the cleaned substring.
    Space Complexity: O(n) for storing the reversed copy and cleaned list.
    """
    # Create a new list with only alphanumeric characters in lowercase
    valid_chars = [c.lower() for c in s if c.isalnum()]

    return "".join(valid_chars) == "".join(reversed(valid_chars))

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "No 'x' in Nixon",
        "",
        "Was it a car or a cat I saw?",
        "madam",
        "123 21"
    ]

    # Run both implementations on the sample values and print results
    for test_string in test_cases:
        result_tp = is_palindrome_two_pointers(test_string)
        result_ss = is_palindrome_slicing(test_string)

        if result_tp == result_ss:
            status = "MATCH"
        else:
            # This should theoretically not happen as both implement the same logic
            status = "MISMATCH (Internal Error)" 

        print(f'Input: "{test_string}"')
        print(f'Two-Pointer Result: {result_tp}')
        print(f'Slicing Result: {result_ss}')
        print(f'Result Status: {status}\n')