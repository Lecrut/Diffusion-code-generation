def swap_characters(s: str) -> str:
    """
    Swaps every adjacent pair of characters in a string in place (conceptually, 
    as strings are immutable in Python, this returns a new string with the swaps applied).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string where every two-character sequence is swapped.
             If the length of the string is odd, the last character remains unchanged.
             
    Time Complexity: O(n)
    Space Complexity: O(n) for creating the result list and joining it back to a string.
    
    Note: Since Python strings are immutable, "in-place" modification results in 
    returning a new string object rather than modifying the original variable's reference directly.
    """
    if not s:
        return ""

    # Convert string to a list for mutability (O(n) space)
    char_list = list(s)
    
    # Iterate over the list with step 2, swapping pairs in place (O(n/2) iterations -> O(n))
    n = len(char_list)
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

    # Join the list back into a string (O(n)) and return it.
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_cases = [
        "abcdef",   # Expected: 'bcafed' -> ('ab','cd','ef') swapped -> 'ba', 'dc', 'fe' wait, logic check below.
                   # Correction on expectation based on prompt "swaps positions of every adjacent pair":
                   # Input: a b c d e f
                   # Pairs: (a,b), (c,d), (e,f)
                   # Swapped pairs: ba, dc, fe -> Result: badcfe. Let's re-verify logic in code mentally.
        "hello",    # Expected: 'olhel' -> ('he','ll') swapped to 'eh', last 'o' stays -> ehlo? No.
                   # Pairs: (h,e), (l,l). Swapped: (e,h), (l,l) + o -> ehllo. Wait, indices 0-1 and 2-3.
                   # h(0)e(1) l(2)l(3) o(4)
                   # Swap 0<->1: eh... Swap 2<->3: ...ll (no change). Result: ehllo? 
                   # Let's trace code logic carefully later in thought process.
        "a",         # Expected: 'a' -> no pairs, returns same.
    ]

    for test_input in test_cases:
        result = swap_characters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Output: '{result}'\n")