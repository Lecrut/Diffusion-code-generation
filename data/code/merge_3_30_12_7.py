import sys

def swap_adjacent_chars(text: str) -> str:
    """
    Swaps every pair of adjacent characters in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with swapped pairs. Single-character strings 
            and empty strings are returned as-is.
    """
    if not text or len(text) < 2:
        return text
    
    result = []
    
    # Process the string in steps of two characters
    for i in range(0, len(text), 2):
        # Append second character then first for each pair
        if i + 1 < len(text):
            result.append(text[i + 1])
            result.append(text[i])
        else:
            # If the last character is alone (odd length string)
            result.append(text[i])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = [
        "abcdef",
        "",
        "a",
        "1234567890",
        "Hello World!",
    ]

    for test_input in sample_inputs:
        output_result = swap_adjacent_chars(test_input)
        print(output_result, end=' ')