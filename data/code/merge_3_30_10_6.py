def swap_characters(s: str) -> str:
    """
    Swaps adjacent pairs of characters in the input string in place.
    
    If a pair is incomplete (i.e., odd number of characters), 
    the last character remains unchanged to avoid index errors,
    ensuring O(n) time complexity and best practices for Python strings.

    Args:
        s (str): The input string to process.

    Returns:
        str: A new string with adjacent pairs swapped. Note that while
             the task asks to modify "in place", immutable strings in 
             Python necessitate creating a new object; this function returns 
             the result directly as per standard Python patterns for string manipulation,
             which is considered efficient and correct behavior when true mutability isn't available.

    Time Complexity: O(n) where n is the length of the input string.
    Space Complexity: O(n) to store the resulting list/converted characters.
    """
    # Convert string to a list for mutability, then perform swaps in pairs
    chars = list(s)
    
    # Iterate up to half the length with step 2 (every second character is processed as part of a pair)
    for i in range(0, len(chars), 2):
        # Check if there's a next character to swap
        if i + 1 < len(chars):
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    test_cases = [
        "hello",      # Odd length: 'he' <-> 'lo', 'o' stays
        "abcdefg",    # Pairs: ab, cd, ef -> bacdefg; wait logic check: a<->b, c<->d... result should be bahcdfe? No. 
                     # Let's trace carefully: input abcdefg (odd)
                     # 0('a'),1('b') swap -> ba
                     # 2('c'),3('d') swap -> dc
                     # 4('e'),5('f') swap -> fe
                     # 6('g') stays. Result: badcfeg? No, indices: 
                     # i=0: chars[0],chars[1] = 'b','a'
                     # i=2: chars[2],chars[3] = 'd','c'
                     # i=4: chars[4],chars[5] = 'f','e'
                     # Final list: ['b', 'a', 'd', 'c', 'f', 'e', 'g'] -> "badcfeg"
        ",!@#",       # Even length, all pairs swapped. "! ,@" becomes "@,! ,"? No: 
                     # 0(','),1('!') swap -> '! ,'
                     # 2('@'),3('#') swap -> '# @'
                     # Result: "# @" + "!" + "," ?? Wait trace again.
                     # Input: ", !, @, #" (with spaces for clarity in thought) actually string is ",!@#" 
                     # len=4. i=0: chars[0](','),chars[1]('!') -> swap -> ['!', ',', ...]
                     # Wait index 0 is ',' and 1 is '!'. Swap makes it '!' then ','. So "!" + "," + "#" + "@"? No.
                     # Original indices: 0:',', 1:'!', 2:'@', 3:'#' 
                     # After swap at i=0: chars[0]='!', chars[1]=',' -> "!," ... wait no, char at 1 is '!' and char at 0 is ','. Swapping them puts '!' at 0 and ',' at 1.
                     # So prefix becomes "!" + ",". 
                     # Next i=2: '@' and '#'. Swap makes '#' then '@'. 
                     # Result string: "!,#@"? No, chars[0]='!', chars[1]=',', chars[2]='#', chars[3]='@'. -> "!,#@"
        "aabbcc",     # Even length. aa->aa (swapped same), bb->bb... actually 'ab' swap order matters if distinct. 
                     # Input a,a,b,b,c,c. i=0: s[0],s[1] are 'a','a'. Swap -> no change visually but logic holds.
                     # Result remains "aabbcc". But wait, input is pairs of same chars? Yes.
    ]

    for test_input in test_cases:
        result = swap_characters(test_input)
        print(f"Input: {test_input!r} => Output: {result!r}")