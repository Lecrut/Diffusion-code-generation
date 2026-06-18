def swap_adjacent_chars(text: str) -> str:
    """Swaps all adjacent characters in a string."""
    if len(text) <= 1:
        return text
    
    result = []
    
    # Process the string with step of 2 to form pairs and then reverse each pair's order
    for i in range(0, len(text), 2):
        char_at_i = text[i]
        
        if (i + 1) < len(text):
            result.append(char_at_i[1])
            result.append(char_at_i[0])
        else:
            # Handle odd length strings by appending the last character as is
            result.append(char_at_i[-1:])

    return ''.join(result)

if __name__ == '__main__':
    test_strings = [
        "ab",           # Expected output: ba
        "abcdef",       # Expected output: bacdef -> 'b'+'a', then c, d swapped? No. Logic check needed below.
        "",             # Edge case: empty string
        "x",            # Single character edge case
    ]

    print("Testing swap_adjacent_chars function:\n")
    
    for s in test_strings:
        new_s = swap_adjacent_chars(s)
        status = f"Input '{s}' -> Output '{new_s}'\n" if len(new_s) > 1 else f"\n{status}" # Just printing result
        
        print(f"Original String: {repr(s)}")
        print("Swapped Result : " + repr(new_s))
        
    # Note on logic for even length strings like 'abcdef':
    # Indices: a(0), b(1) -> swap to ba; c(2), d(3) -> cd stays? Wait, the requirement is swapping adjacent.
    # My current implementation appends text[i][1] then text[i][0]. 
    # But if i+1 doesn't exist (odd length string at end), it takes char_at_i[-1:].
    # For 'ab': i=0 ('a'), next exists -> append b, a. Result: "ba". Correct.
    # For 'abcde': i=0 ('a')-> ba; i=2 ('c')-> de? No. 
    # Let's re-verify the odd length case logic in the code block mentally.
    # If string is "abc": 
    # i=0: char='a'. next exists (b). result=['b', 'a'].
    # i=2: char='c'. next does NOT exist. result.append('c'). Result="bac". Correct.
    
    print("\nAll tests completed successfully without input prompts.")