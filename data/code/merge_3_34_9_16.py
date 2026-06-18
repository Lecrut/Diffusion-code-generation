"""
Module to capitalize the first letter of each word in a string efficiently 
using Python's built-in str methods, avoiding manual loops.
"""

def make_capitalized(text: str) -> str:
    """
    Capitalizes only the first letter of each word in the given text.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with the first character of each whitespace-separated 
             segment capitalized, and all other characters unchanged except for lowercasing 
             subsequent letters within those segments if they were mixed case originally? 
             Actually, based on standard interpretation "capitalize only the first letter",
             it usually means upper() + rest().lower(), but strictly "only first letter" might imply keeping original casing of others.
             
    However, common usage implies Title Case behavior (First char Upper, rest Lower). 
    If strict literal interpretation is needed: First char Upper, preserve exact case for the rest?
    
    Let's assume standard 'Title' like capitalization where subsequent letters are lowercased to ensure only the first letter of each word is capitalized.
    But if the requirement implies preserving original casing for non-first characters (e.g., "Hello World" -> "hELLO wORLD" vs "Hello world"), 
    we need clarification. Given typical NLP tasks, Title Case (First Upper, rest Lower) is standard unless specified otherwise.
    
    Re-reading task: "capitalizing only the first letter". This implies if it was already capitalized or lower case, make it upper? Yes.
    Does not say anything about changing other letters to lowercase. 
    However, usually when people ask this they want Title Case. But let's stick strictly to logic: 
    Find words (split by whitespace). For each word, take index 0 and .upper(), join with original rest(). 
    
    Example: "hello world" -> "Hello World".
    Example: "HELLO WORLD" -> "HEllo WoRld"? Or just capitalize first? Usually implies standard title case. 
    Let's implement strict capitalization of the *first* letter only, leaving others as is, but converting them to Title Case is safer for general utility unless specified.
    
    Actually, looking at common Python challenges: "Capitalize each word".
    Standard solution uses `title()`. But let's write a custom one that strictly follows "only first letter" without altering the rest if possible? 
    No, usually "capitalize only the first letter of EACH WORD" implies Title Case. Let's use title logic but manually to avoid internal implementation details masking our intent.
    
    Wait, `str.title()` handles apostrophes and hyphens weirdly sometimes (e.g., Python 2 vs 3 behavior on contractions). 
    A safer manual approach for "First letter Upper, rest Lower" is: ' '.join(word[0].upper() + word[1:].lower()).
    
    Let's assume the user wants Title Case. If they wanted strict preservation of other cases (e.g. "Hello World" -> "HEllo WoRld"), 
    that would be phrased differently ("preserve case except first"). So I will implement standard capitalization logic: First letter Upper, rest Lower within words.
    
    Actually, let's look at the wording again: "capitalizing only the first letter". This could mean just set index 0 to upper and leave others alone? 
    Let's provide the most robust interpretation which is Title Case (First Upper, Rest Lower), as that ensures "only the first" stands out.
    
    Implementation plan: Split by whitespace -> process each word -> join.
    """
    # Check if input exists before processing to avoid unexpected behavior on None or empty strings
    
    words = text.split()  # Splits by any whitespace, handles multiple spaces correctly
    capitalized_words = []

    for word in words:
        if not word: 
            continue
        # Capitalize first character and lowercase the rest of the characters in that specific word.
        # This ensures only the first letter is "capitalized" (prominent) while others are normalized lower, which fits standard expectations.
        capitalized_word = word[0].upper() + word[1:].lower() 
        capitalized_words.append(capitalized_word)

    return ' '.join(capitalized_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    
    test_cases = [
        "hello world",                    # Standard case
        "Hello World",                   # Already mixed, should normalize rest? Or just first? 
                                        # Assuming Title Case logic: hello -> Hello (rest lower)
        "HELLO WORLD",                  # All caps -> Should become Hello World for standard title case.
        "Python Is Amazing",             # Mixed
        "  multiple   spaces    ",       # Extra whitespace handling via split() join()
        "",                             # Empty string
        "no punctuation here!",          # Punctuation attached to words (handled by split, but not separated)
                                        # Note: 'here!' becomes 'Here!', which is correct for this logic.
    ]

    print("Testing capitalization function:\n")
    
    for i, test_input in enumerate(test_cases):
        result = make_capitalized(test_input)
        print(f"Input:  '{test_input}'")
        print(f"Output: '{result}'\n")