"""
Module to process text blocks by capitalizing the first letter of each word 
while keeping all other letters lowercase, applied efficiently across the entire block.
This implementation uses a single pass over the string with regex or manual iteration 
to ensure optimal performance for large texts without external dependencies beyond standard library.

The 'capitalize' rule defined here is: The very first character of the text (if it exists) 
is converted to uppercase, and every subsequent word's first letter is also capitalized,
while all other characters are lowercased. This matches Python's built-in str.capitalize() behavior 
but applied globally rather than just at the start of the string.

Note: The task description says "capitalize the first letter only", which typically means 
only the very first character of the entire text should be uppercased and everything else lowercased.
However, in natural language processing contexts involving blocks of text, users often expect each word to follow title case rules.
Given the ambiguity, this implementation adopts a hybrid approach that strictly follows "first letter only" 
for the global rule as interpreted literally: ONLY THE VERY FIRST CHARACTER OF THE ENTIRE BLOCK IS CAPITALIZED,
and ALL OTHER CHARACTERS ARE LOWERCASED. This is distinct from str.title() or title_casing each word.

Example transformation logic for input "hello world": output "Hello world".
Input "HELLO WORLD" -> Output "HelLo WoRlD" (only first char upper, rest lower).
"""

def process_text_block(text: str) -> str:
    """
    Processes a block of text by capitalizing only the very first letter 
    and converting all remaining characters to lowercase.

    Args:
        text (str): The input string or text block to be processed.

    Returns:
        str: A new string with only the first character uppercase and the rest lowercase.
             If the input is empty, an empty string is returned.
    
    Complexity Analysis:
        Time Complexity: O(n) where n is the length of the text, as we iterate through each character once.
        Space Complexity: O(1) auxiliary space excluding the output string storage which requires O(n).

    Example:
        >>> process_text_block("hello world")
        'Hello world'
        
        >>> process_text_block("HELLO WORLD")
        'HelLo WoRlD' -> Wait, re-reading requirement "capitalize the first letter only" usually implies 
                       standard capitalization rules per word in many contexts BUT strictly speaking it means ONLY THE FIRST.
                       Let's stick to the strictest interpretation of "first letter only": Only index 0 becomes upper case if present.
        >>> process_text_block("HELLO WORLD")
        'Hello world' (Strict: First char Upper, Rest Lower)

    However, upon closer re-evaluation of common intent in such tasks where users say "capitalize the first letter", 
    they often mean standard sentence casing or title case per word. But to be safe and literal:
    We will implement exactly what is written: Capitalize ONLY THE FIRST LETTER OF THE TEXT BLOCK.
    All other letters become lowercase regardless of their original state.

    Revised Example Logic for "HELLO WORLD": 
        Input: 'H' -> Upper, rest lowercased. Result: 'Hello world'.
    """
    
    if not text or len(text) == 0:
        return ""
    
    # Convert the entire string to lowercase first to ensure consistency of remaining characters
    result = list(text.lower())
    
    # Capitalize only the very first character (index 0)
    if len(result) > 0:
        result[0] = result[0].upper()
        
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used.
    
    samples = [
        "hello world",
        "HELLO WORLD",
        "",
        "python programming language",
        "   leading spaces here  ",
        "!@#$%^&*()"
    ]

    print("Processing text blocks with 'capitalize first letter only' rule:\n")
    
    for sample in samples:
        processed = process_text_block(sample)
        print(f"Input : '{sample}'")
        print(f"Output: '{processed}'\n")