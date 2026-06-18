def swap_characters(s: str) -> None:
    """
    Swaps every adjacent pair of characters in a string in place.
    
    If there is an odd number of characters, the last one remains unchanged.
    Modifies the input string directly and returns it (via side effect).

    :param s: Input string to swap characters from.
    """
    char_list = list(s)
    
    # Iterate with a step of 2 up to len(char_list) - 1
    for i in range(0, len(char_list), 2):
        if i + 1 < len(char_list):
            # Swap characters at index i and i+1
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
    
    return "".join(char_list)

if __name__ == '__main__':
    # Sample string: "abcdefg" -> expected output: "bacdfe g" (last 'g' stays)
    sample_input = "abcdefg"
    
    result_str = swap_characters(sample_input)
    
    print(f"Input: {sample_input}")
    print(f"Output: {result_str}")

# Additional test cases for verification within the module logic if expanded later,
# but strictly keeping to single return as per task requirements.