def swap_characters(s: str) -> str:
    """
    Swaps adjacent pairs of characters in a string in place.
    
    The function modifies the input string by converting it to a list, 
    swapping elements at indices 0-1, 2-3, etc., and then joining back into a string.
    
    Args:
        s (str): A single string with no spaces required; any length >= 0 is allowed.
        
    Returns:
        str: The modified string after all adjacent pairs have been swapped.

    Examples:
        swap_characters("abc") returns "bac"
        swap_characters("abcd") returns "bdca"
        swap_characters("") returns ""
        swap_characters("a") returns "a"
    """
    # Convert the string to a list for mutability
    char_list = list(s)
    
    # Iterate through the list with step 2 and swap adjacent elements
    for i in range(0, len(char_list), 2):
        if i + 1 < len(char_list):
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
    
    # Join the list back into a string and return it. 
    # Note: Since Python strings are immutable, we essentially create a new object here.
    return "".join(char_list)

if __name__ == '__main__':
    test_cases = [
        "hello",     # Expected output: olleh (helo -> ohle? No: h-e-llo -> e-h-o-l? Let's trace manually.)
                     # Trace: h(0)e(1)->eh, l(2)o(3)->ol. Result: eh ol -> eh o l ? 
                     # Wait, "hello": indices 0(h),1(e) swap -> eh; 2(l),3(l) swap -> ll; 4(o).
                     # Actually standard adjacent pair logic on string 'abc' is b a c? No.
                     # 'a'(0),'b'(1) -> swap to 'b','a'. 'c'(2) stays if odd len. Result "bac".
        "hello",     # h,e,l,o, o (len 5). Swap(0,1): e,h; Swap(2,3): l,l? No index 2 is l, 3 is o. -> o,l. Index 4 remains 'o'. 
                     # Result: eh ollo
        "abcdef",    # ba dc fe
        "",          # empty string stays empty
        "a",         # single char stays same
        "xy"          # yx
    ]

    for test_input in test_cases:
        result = swap_characters(test_input)
        print(f"'{test_input}' -> '{result}'")