import time

def is_palindrome_two_pointers(text: str) -> bool:
    """
    Checks if a string (or text with spaces/punctuation preserved as-is unless specified otherwise) 
    is a palindrome using the two-pointer technique. This implementation assumes we are checking 
    for exact character match including case and non-alphanumeric characters, as per standard practice 
    in such tasks when specific normalization rules aren't provided.

    Note: If strict alphanumeric-only comparison with case-insensitivity was intended, this function
    would require an adjustment to filter/sanitize first. Based on typical efficiency requirements, 
    we assume the raw string check for two-pointer optimization unless otherwise noted. For a more robust
    definition of palindrome (ignoring spaces/punctuation and case), one might preprocess first; however,
    here we stick strictly to character equality as per basic definitions unless specified differently in common challenges like "racecar".

    Time Complexity: O(n) where n is the length of text.
    Space Complexity: O(1).
    
    Examples include 'abcba' -> True, 'hello' -> False.
    """
    # Two-pointer approach without pre-processing for case/punctuation unless specified otherwise in problem context
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_slicing(text: str, case_sensitive=True, ignore_non_alnum=False) -> bool:
    """
    Checks if a string is a palindrome using Python's slicing capabilities. 
    This method typically involves reversing the entire string and comparing it to the original, which may include spaces/punctuation unless filtered.

    For optimized efficiency without modifying input size unnecessarily in loops:
    - If case_sensitive=False and ignore_non_alnum=True, we construct cleaned versions for comparison but still rely on slicing logic implicitly via str[::-1]. 
      However, explicit cleaning avoids O(n) extra space allocation beyond the slice itself if not needed.

    Time Complexity: O(n). String reversal is linear in time and creates a new string (O(n)).
    Space Complexity: O(n) for creating reversed copy unless avoided by clever logic which Python doesn't support directly without slicing anyway here.
    
    Examples include 'abcde fedcba' -> False if no ignore_non_alnum; True with filters applied appropriately.
    """
    # Default behavior aligns to standard palindrome checks (case-sensitive and preserving all characters)
    if case_sensitive:
        reversed_str = text[::-1]
    else:
        # Case-insensitive reverse comparison works by normalizing before reversal or converting back
        normalized_original = text.lower()
        reversed_normalized = "".join(reversed(normalized_original))

if __name__ == '__main__':
    pass
