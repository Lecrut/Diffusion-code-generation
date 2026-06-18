import time

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
        
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) as no additional data structures are used beyond pointers.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from both ends to match case-insensitive palindromes like "A man, a plan..."
        if not s[left].isalnum():
            left += 1
            continue
            
        if not s[right].isalnum():
            right -= 1
            continue
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    samples = [
        "A man, a plan, a canal: Panama",
        "race car",
        "hello world",
        "",
        "Was it a car or a cat I saw?",
        "Madam",
        "not a palindrome"
    ]

    start_time = time.time()
    
    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")
        
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"\nTotal execution time: {elapsed:.6f} seconds")