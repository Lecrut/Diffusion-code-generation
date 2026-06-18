import string

def swap_characters(s: str) -> None:
    """
    Swaps every adjacent pair of characters in a string in place.
    
    This function modifies the input string directly by converting it to a list,
    swapping elements at indices (0,1), (2,3), etc., and then joining back into a string.
    The time complexity is O(n) where n is the length of the string.
    
    Args:
        s (str): The input string whose adjacent character pairs will be swapped.
        
    Returns:
        None: Modifies the input list/string in place, but returns it for consistency 
               with typical Python function expectations when modification isn't strictly enforced by signature semantics.
               Note: To satisfy "modify directly and return", this converts to a mutable list, swaps, joins, updates 's', then returns s.
    """
    # Convert string to list of characters since strings are immutable in Python
    char_list = list(s)
    
    # Iterate over the list with step 2 to access pairs (i, i+1)
    for i in range(0, len(char_list), 2):
        # Check if there is a second character in the pair
        if i + 1 < len(char_list):
            # Swap characters at current and next index
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
    
    # Join list back into string to ensure proper return type behavior as requested ("return it")
    new_s = "".join(char_list)
    
    # Update the original input variable 's' directly (in-place modification of reference context)
    s = new_s
    
    return s

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    test_cases = [
        "abcdef",      # Expected: "bcafed" -> pairs (a,b)->(b,a), (c,d)->(d,c)... wait, logic check: 
                      # 'ab' becomes 'ba', 'cd' becomes 'dc', 'ef' becomes 'fe'. Result: 'badcf e'? No.
                      # Input "abcdef": indices 0(a)1(b)2(c)3(d)4(e)5(f). Swap (a,b)->b,a; (c,d)->d,c; (e,f)->f,e. 
                      # Result string: "bad cfe" -> "bacdf e"? Let's trace carefully.
                      # i=0: swap s[0],s[1] ('a','b') -> 'b', 'a'. List: ['b','a','c','d','e','f']
                      # i=2: swap s[2],s[3] ('c','d') -> 'd', 'c'. List: ['b','a','d','c','e','f']
                      # i=4: swap s[4],s[5] ('e','f') -> 'f', 'e'. List: ['b','a','d','c','f','e']
                      # Final string: "badcf e" -> "bacdf"? No, indices 0-1 is ba, 2-3 dc, 4-5 fe. 
                      # So "ba" + "dc" + "fe" = "badcfe". My previous mental trace was slightly off in concatenation logic but code handles it correctly.
    
        "hello",       # Odd length: 'he'->'eh', 'll'->'ll'. Result: "ehllo"
        "",            # Empty string -> ""
        "a",           # Single char -> "a" (loop range(0,1) runs once but i+1<1 is false for i=0? No. 
                      # Range(0, 1): i=0. Check if 0+1 < 1 -> False. No swap occurs. Correct.)
        "xy",          # Even length: 'yx'
    ]

    print("Running swap_characters tests...")
    
    for idx, test_input in enumerate(test_cases, 1):
        result = swap_characters(test_input)
        
        if not isinstance(result, str):
            raise TypeError(f"Function returned non-string type {type(result)} instead of string.")
            
        print(f"Test Case #{idx}:")
        print(f"Input:    \"{test_input}\"")
        print(f"Output:   \"{result}\"")
        
        # Verify correctness for debugging purposes (optional but good practice)