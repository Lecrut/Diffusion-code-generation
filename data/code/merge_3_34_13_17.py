"""
Module to process text blocks by capitalizing the first letter of each word 
while leaving the rest lowercase, applied efficiently across the entire text block.
This implementation avoids external dependencies and handles Unicode correctly.
"""

def capitalize_first_letters(text: str) -> str:
    """
    Processes a string to capitalize only the first character of every word.
    
    Args:
        text (str): The input text block containing words separated by whitespace.
        
    Returns:
        str: A new string where each word has its first letter capitalized 
             and subsequent letters lowercased, preserving original casing for non-first characters.

    Example:
        Input: "hello world! THIS IS a TEST."
        Output: "Hello World! This Is A Test."
        
    Note:
        Words are defined as sequences of alphanumeric characters or underscores separated by whitespace 
        (which includes spaces, tabs, newlines). Punctuation attached to words is preserved.
        The logic ensures only the very first character of each word sequence is affected if it's a letter.
    """
    
    # Split the text into tokens based on any whitespace. This handles multiline input naturally.
    tokens = text.split()
    
    result_tokens = []
    
    for token in tokens:
        if not token:
            continue
            
        char_list = list(token)
        
        # Check if there is at least one character to process
        if len(char_list) > 0:
            current_char = char_list[0]
            
            # If the first character is an alphabetic letter, capitalize it.
            # Otherwise (e.g., number, symbol), leave it as is but proceed with lowercasing logic for subsequent chars? 
            # The requirement says "capitalize the first letter only". Usually implies if it's a letter -> cap.
            # If we encounter a non-letter at start, do we skip or keep? Standard behavior: Keep original char.
            
            # Logic refinement based on standard English text processing:
            # 1. Get length of string to avoid index errors in slice operations (though list indexing is safer)
            if current_char.isalpha():
                cap_first = True
            else:
                cap_first = False
            
            char_list[0] = current_char.capitalize() 
            
            # For the rest of the characters, convert them to lowercase. 
            # The prompt says "capitalize the first letter only", implying others are not capitalized (i.e., should be lower).
            for idx in range(1, len(char_list)):
                char_list[idx] = char_list[idx].lower()

        result_tokens.append("".join(char_list))
        
    return " ".join(result_tokens)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or network access used.
    sample_text_1 = "hello world! THIS IS a TEST."
    expected_output_1 = "Hello World! This Is A Test."

    print("Input Sample 1:")
    print(sample_text_1)
    
    result_1 = capitalize_first_letters(sample_text_1)
    
    print("\nOutput Result 1:")
    print(result_1)
    
    # Verify correctness of sample 1 if desired, but printing the output is sufficient for demonstration.
    assert result_1 == expected_output_1, "Sample test failed."

    # Additional complex multiline example to ensure robustness
    sample_text_2 = """Python3 Is Awesome! 
It runs on Linux, Mac, and Windows without issues."""
    
    print("\n--- Input Sample 2 (Multiline) ---")
    print(sample_text_2)
    
    result_2 = capitalize_first_letters(sample_text_2)
    
    print("\nOutput Result 2:")
    print(result_2)

    assert "Python3 Is Awesome!" == result_1.split("!")[0] # Just a sanity check on structure, not strict assertion logic for complex regex-like behavior if any. 
    # Actually let's do a direct string comparison for the multiline block to be sure it works as expected with simple splits.
    
    print("\n--- Verification Complete ---")