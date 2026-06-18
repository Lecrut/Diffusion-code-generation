#!/usr/bin/env python3
"""
Script to print the first letter of each word in a given string,
handling various whitespace scenarios including leading/trailing spaces,
multiple consecutive spaces, tabs, and newlines implicitly handled by split().

This module does not use input(), sys.stdin for interactive reading, 
or any external dependencies. It is designed to be run directly with sample data.
"""

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first letter of each word from the input string.
    
    Args:
        text (str): The input string containing words separated by whitespace.
        
    Returns:
        list[str]: A list of strings, where each element is the lowercase 
                   first character of a non-empty word found in the input.
                   
    Notes:
        - Uses split() which handles all Unicode whitespace characters and multiple spaces efficiently.
        - Converts to lower case for consistency unless specific casing was requested (not specified).
          Here we assume standard behavior where 'first letter' implies the character itself, 
          but typically such tasks imply a normalized output like lowercase letters if not strictly defined.
          To be robust against mixed cases while keeping it simple: returns characters as is? 
          Let's re-read "first letter". Usually means A-Z or a-z. 
          If the input has numbers/symbols inside words, split() keeps them attached.
          The task says 'letter', implying alphabetic only? Or just first token char?
          Given "robust" and "efficiently", usually implies taking the first character of each word string.
          Let's return exactly that: the first character of each non-empty word found by splitting on whitespace.
    """
    # split() without arguments handles all whitespace types (space, tab, newline, etc.) 
    # and automatically filters out empty strings resulting from consecutive spaces.
    words = text.split()
    
    result = []
    for word in words:
        if not isinstance(word, str):
            continue
            
        if len(word) > 0:
            first_char = word[0]
            # The prompt asks for "first letter". Strictly speaking, '2' is a digit and '@' is a symbol.
            # However, in most string processing contexts without further specification (like regex [a-zA-Z]), 
            # the intent is usually the first character of the word token.
            # If we strictly filter for alphabetic characters only:
            import unicodedata
            char = first_char
            
            if 'A' <= char.lower() <= 'Z':
                result.append(char)
        else:
            continue
    
    return result

def main():
    """
    Main execution block.
    Runs with hard-coded sample values to demonstrate functionality without user input.
    
    Sample inputs cover:
    - Normal spaces
    - Multiple consecutive spaces
    - Leading/trailing whitespace
    - Mixed case words
    - Words containing non-alphabetic characters (to test strict vs loose interpretation)
      We will stick to returning the first character of each word token, 
      as "letter" in common parlance often loosely refers to 'character' or the specific task implies [a-zA-Z] logic.
      
      Let's refine: If I say "first letter", do you mean A-Za-z only? Or just start char?
      Example input: "Hello World 123 Test" -> H, W, ?, T? 
      Usually in these coding tasks, if they want letters specifically, they specify regex.
      But to be safe and robust as requested: I will check if the character is alphabetic. 
      If not (e.g., a number), it might not be considered a "letter".
      
      Revised logic for strict interpretation of 'letter': Only include words starting with A-Z or a-z.
    """
    
    # Hard-coded sample values ensuring no user input, args, stdin, etc. are used.
    samples = [
        "  Hello World   ",          # Leading spaces and trailing space + multiple internal spaces
        "Python is Awesome",         # Normal sentence with mixed case
        "123 Numbers! @Symbols# Data", # Words starting with non-letters (to test 'letter' constraint)
    ]

    for i, sample_input in enumerate(samples):
        print(f"\n--- Sample {i + 1} ---")
        print("Input:", repr(sample_input))
        
        letters = get_first_letters(sample_input)
        
        if not letters:
            output_str = "No alphabetic words found."
        else:
            # Joining the results with a space for clean printing, or just printing them.
            # The task says "prints the first letter", implying print(letters[0]), but usually implies all of them.
            # Let's print each on a new line to be clear about which word produced it, 
            # OR join them if that was implied by 'the' (singular) result set?
            # "Prints the first letter..." -> Plural context suggests listing them or printing one per word.
            # Standard output for such tasks: print each character separated by space or new line.
            # Let's use a single string joined by spaces if possible, but since we need to show mapping clearly? 
            # Actually, simplest robust interpretation: Print the characters found, usually on separate lines or one per word logic.
            # Given "the first letter of each word", it implies a sequence.
            
            output_str = "".join(letters)
        
        print("Output:", output_str if isinstance(output_str, str) else letters)

if __name__ == '__main__':
    main()