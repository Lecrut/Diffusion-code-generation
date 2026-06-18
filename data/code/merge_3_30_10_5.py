def swap_characters(s: str) -> None:
    """
    Swaps adjacent pairs of characters in a string in place.
    
    Args:
        s (str): The input string to modify.
        
    Returns:
        None: Modifies the string directly and returns it for consistency with functional style, 
              though per task requirement 'return' is included which implies returning self or value.
              Given Python strings are immutable, this function cannot truly modify in-place without
              converting to a list first then back to string if true mutability was required externally.
              
    However, since the prompt asks for "modify input directly", and strings are immutable:
    We will convert s to a list of characters, swap them, join them into a new string, 
    but assign it back only if we were allowed mutable structures which we aren't without side effects on caller.
    
    Since Python doesn't support true in-place mutation for str objects (only lists), and returning the result 
    while saying "modify input" implies reassignment or using list buffer...
    
    To strictly satisfy "swap ... in place" behavior while adhering to immutability:
    We will perform the swaps on a list derived from s, then return the resulting string.
    The phrase 'in place' is semantically impossible for strings without external state change (like reassigning local var), 
    so we interpret as processing and returning immediately with O(n).

    Time Complexity: O(n) where n is len(s) - one pass through halves of pairs.
    Space Complexity: O(k) if k > 0 due to list creation, but unavoidable for string manipulation in Python unless using bytearray-like logic which isn't standard str ops.

    Note on "in place": 
        Since strings are immutable, true in-place modification requires converting to a mutable type like `list` or `bytearray`,
        performing swaps, then reconstructing the result. Without external mutation (like assigning back to caller's variable),
        only return-based updates happen here as per Python semantics.

    Implementation converts input string to list of chars for mutability:
        - Iterate over indices in steps of 2 up to length // 2.
        - Swap s[i] and s[i+1].
        Join back into a new string returned by this function (to match return requirement). 
    """
    # Convert to list since strings are immutable; allows true "in-place" style swapping via mutable container
    chars = list(s)
    
    n = len(chars)
    i = 0
    
    while i < n - 1:
        if i + 1 >= n:
            break
        
        # Swap adjacent characters at indices i and i+1
        chars[i], chars[i+1] = chars[i+1], chars[i]
        
        # Move forward by two to process next pair (if exists) or just one more? 
        # The requirement says "every adjacent pair", meaning pairs (0,1), (2,3)... not overlapping swaps like bubble.
        i += 2

    return "".join(chars)

def main():
    """Main execution block with hard-coded samples."""

if __name__ == '__main__':
    pass
