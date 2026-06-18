def reverse_adjacent_swaps(s: str) -> str:
    """
    Takes a string and swaps every pair of adjacent characters (e.g., index 0 with 1, 
    then 2 with 3, etc.) and returns the resulting string.
    
    The time complexity is O(n), where n is the length of the input string.
    We only iterate through the string once in steps of two.
    """
    # Convert the string to a list for mutability since strings are immutable in Python
    char_list = list(s)
    
    limit = len(char_list) // 2
    
    # Iterate over each pair and swap characters at index i with i+1
    for i in range(limit):
        j = i + 1
        if j < len(char_list):
            # Swap the current character with its adjacent one
            char_list[i], char_list[j] = char_list[j], char_list[i]
    
    # Join the list back into a string and return it as an immutable sequence of characters is needed for output
    swapped_s: str = ''.join(char_list)
    return swapped_s

if __name__ == '__main__':
    sample_inputs = ["abcd", "hello-world", "a"]
    
    # Run the function on each sample input and print the result directly without any interactive prompts.
    for test_str in sample_inputs:
        result = reverse_adjacent_swaps(test_str)
        original = f"Original String: {test_str}"
        modified = f"After Swapping Adjacent Pairs: '{result}'"

        # Outputting results to confirm the operation was performed correctly without user input or file access.
        print(original + "\n" + modified + "\n")