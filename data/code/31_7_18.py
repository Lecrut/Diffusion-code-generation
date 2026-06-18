import sys

def is_palindrome_optimized(s: str) -> bool:
    """
    Check if a string is a palindrome by comparing it with its reversed version,
    optimized to minimize memory usage by slicing only the necessary parts implicitly 
    (Python's slice creates new strings, but no complex data structures are used).

    This approach compares s with s[::-1]. For very large strings where creating 
    a full copy is undesirable in tight loops or embedded systems, an iterator-based
    two-pointer comparison would be superior for memory. However, since the task explicitly
    asks to compare "the original string with its reversed version", we follow that logic.

    Note: While s[::-1] creates a new string (O(N) space), this is standard and 
    cleaner than manual character access unless strict O(1) auxiliary space is demanded.
    
    If strictly O(1) memory relative to input size were required without creating the reverse,
    an iterative two-pointer approach would be used instead:

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]: return False
            left += 1
            right -= 1
        return True
        
    The prompt specifically requests comparing with the reversed version. 
    To balance readability and memory constraints as best as possible for a general purpose script,
    we will use the two-pointer approach which is effectively checking against the reverse logic
    but uses O(1) extra space (excluding input storage), satisfying "minimizing memory usage" better than slicing.

    Actually, re-reading: "comparing the original string with its reversed version". 
    This usually implies creating the reversed copy in naive interpretations. 
    However, to truly minimize memory as requested while adhering to Python's capabilities:
    
    Let's stick to the literal instruction of comparing against a reverse if possible, 
    but since 'reversed()' or slicing creates copies, and we need O(1) ideally for optimization:
    
    The most optimized solution in Python that avoids allocating a reversed copy is the two-pointer method.
    It simulates comparing s[i] with s[len-1-i], which is equivalent to checking against the reverse 
    without actually constructing it. This minimizes memory usage significantly compared to slicing.

    @param s: The input string to check
    @return: True if palindrome, False otherwise
    """
    # Two-pointer approach for O(1) space complexity (excluding input storage)
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        "radar",           # Palindrome -> True
        "hello",           # Not palindrome -> False
        "",                # Empty string is palindrome -> True
        "A man a plan a canal Panama",  # Case sensitive? The problem says 'string'. Usually case-sensitive unless specified. 
                          # We treat as strict character match based on standard definition unless told otherwise.
                          # Let's use lowercase for safety or just the raw input logic: "manaplanacnalpanamA" is not a palindrome in this version if we don't normalize.
                          # The prompt does not ask to ignore case, so we compare strictly.
        "123",             # Not palindrome -> False
        "racecar",         # Palindrome -> True
    ]

    for s in samples:
        result = is_palindrome_optimized(s)
        print(f"'{s}' is a {'palindrome' if result else 'not'} a palindrome")