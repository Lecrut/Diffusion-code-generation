def swap_adjacent_pairs(s):
    """
    Swaps all adjacent character pairs in a string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
             If the length is odd, the last character remains unchanged.
             
    Example:
        Input: "abcd" -> Output: "bdac"
        Input: "abcde" -> Output: "bdc a e" (effectively swapping pairs and keeping tail)
              Actually logic: ab|cd|e -> ba|dc|e -> badce? 
              Let's trace carefully:
              'a','b' swap to 'b','a'; 'c','d' swap to 'd','c'. Last 'e' stays.
              Result: "badce"
    """
    result = []
    
    # Process the string in steps of 2
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            # Swap current character with next one
            result.append(s[i + 1])
            result.append(s[i])
        else:
            # Handle odd length string - append the last single character as is
            result.append(s[i])
            
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        "abcd",
        "abcdefg",
        "",
        "a"
    ]
    
    for test_input in sample_strings:
        modified_output = swap_adjacent_pairs(test_input)
        print(modified_output)