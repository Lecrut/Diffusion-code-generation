import sys

def check_palindrome_optimized(s: str) -> bool:
    """
    Check if a string is a palindrome by comparing it with its reversed version.
    
    This approach creates a full reverse of the input string and compares them,
    which uses O(n) memory in terms of characters but keeps the logic simple 
    and direct as requested for this specific implementation style.

    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    reversed_s = s[::-1]
    
    return s == reversed_s

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or arguments)
    
    test_cases = [
        "radar",           # True palindrome
        "hello",           # False palindrome
        "",                # Empty string is a palindrome
        "A man a plan a canal Panama",  # Case-sensitive usually, but let's see default behavior. 
                          # Standard comparison will return False for mixed case unless specified otherwise.
    ]

    print("Palindrome Check Results:")
    
    for test_string in test_cases:
        is_pal = check_palindrome_optimized(test_string)
        status = "IS" if is_pal else "is not"
        result_str = f"{test_string!r} {status} a palindrome"
        
        # Using !r to show quotes around strings for better debug output 
        print(result_str)

    # Demonstrate with specific complex case handling if needed, 
    # though the core task requested simple original vs reversed comparison.
    
    sample_complex = "Race car!"  # Contains spaces and punctuation
    
    is_sample_pal = check_palindrome_optimized(sample_complex)
    status_samp = "IS" if is_sample_pal else "is not"
    print(f"{sample_complex!r} {status_samp} a palindrome")