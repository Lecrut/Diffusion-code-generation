import time

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome using the two-pointer technique.
    
    This function ignores case differences but considers all characters, including spaces and punctuation.
    It uses O(n) time complexity where n is the length of the string, 
    as it only traverses half of the string to find any mismatched pair.

    Args:
        s (str): The input string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        
        # Move pointers inward until they cross or mismatch found
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1

    return True

if __name__ == '__main__':
    
    sample_strings = [
        "race car", 
        "A man a plan a canal Panama!", 
        "hello world", 
        "", 
        "Madam", 
        "Test"
    ]
    
    for test_str in sample_strings:
        
        start_time = time.perf_counter()
        result = is_palindrome(test_str)
        end_time = time.perf_counter()

        print(f'Input: "{test_str}"')
        print(f'Result: {result}')
        print('Time taken:', f'{(end_time - start_time)*10**6:.2f} microseconds\n', sep='')