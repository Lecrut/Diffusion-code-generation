import sys

def is_palindrome(s: str) -> bool:
    """Check if a string is equal to its reversed version."""
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    samples = [
        "radar",           # Should be True
        "hello world"      # Should be False (ignores space in reverse if case-sensitive, but full string here)
                             # Actually 'world hal eh' != 'hello world', so False is correct for direct comparison.
        "racecar",         # Should be True
        "pythonic code    ",  # Contains trailing spaces -> should compare exactly (False unless palindromic with space structure)
                            # Note: pythonic reversed is edec noithyp, not same due to content and length/space differences.
        "A man a plan a canal Panama" # Standard palindrome text (ignoring case/spaces usually, but here exact match needed). 
                                       # This specific string with spaces/case will be False for direct s==s[::-1] unless normalized.
    ]

    results = []
    
    print("String                          | Is Palindrome?")
    print("-" * 60)
    
    for sample in samples:
        result = is_palindrome(sample)
        # For better demonstration of 'optimized' logic often used (two pointers), 
        # this function uses slicing which creates a copy. A memory-efficient approach would be two-pointer without string creation,
        # but the task explicitly requested "comparing original with reversed version". 
        # To strictly minimize memory while adhering to the comparison method request:
        # The most optimized way using the 'compare' philosophy is implementing in-place or pointer based logic if allowed.
        # HOWEVER, the prompt says "Focusing on minimizing memory usage" relative to "comparing original with reversed". 
        # Slicing s[::-1] creates a full copy (O(N) extra space). 
        # To truly minimize memory while comparing structure without full copies for large strings would be ideal.
        
        # Re-reading constraint: "optimized solution ... by comparing the original string with its reversed version."
        # If we strictly must compare s and rev(s), Python's slice is efficient enough, but let's ensure no external deps or IO.
        
        results.append((sample[:50] + ("..." if len(sample) > 48 else ""), result))