def swap_adjacent_pairs(s: str) -> str:
    """
    Returns a new string where every pair of adjacent characters has been swapped.
    
    Uses slicing to process pairs efficiently without modifying the original string in place.
    If there is an odd number of characters, the last one remains unchanged as it cannot form a complete pair.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with adjacent character pairs swapped.
    """
    # Create list of strings in steps of 2 and join them back together
    return "".join(s[i:i+2][::-1] for i in range(0, len(s), 2))

if __name__ == '__main__':
    sample_input = "abcdef"
    result = swap_adjacent_pairs(sample_input)
    print(result)

# Additional test cases can be verified manually:
# Input: "abcde" -> Output: "bacd e" (last 'e' stays as is due to odd length logic handled by slice step 2 and range stop)
# Note: The implementation above handles even lengths perfectly. For odd lengths like "abc", 
# it produces "bac". Let's verify the behavior for "abc":
# i=0: s[0:2] = "ab" -> reversed is "ba"
# i=2: s[2:4] = "c" (since len(s)=3, slice stops at 3) -> reversed is still "c"
# Result: "bac", which matches the requirement that only pairs are swapped.

# Example trace for sample_input="abcdef":
# i=0: s[0:2]="ab" -> "ba"
# i=2: s[2:4]="cd" -> "dc"
# i=4: s[4:6]="ef" -> "fe"
# Result: "badcfe"