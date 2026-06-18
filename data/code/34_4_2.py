import sys

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes only the first letter of each word in the input text.
    
    Args:
        text (str): The input string containing words to be processed.
        
    Returns:
        str: A new string where the first letter of each word is uppercase,
             and all other characters remain unchanged except for spaces which are preserved.
             
    Logic:
    - Splits the text into words based on whitespace.
    - For each word, converts it to title case but ensures only the very first character
      is uppercased if it exists, while leaving subsequent letters as they were originally (though typical capitalization rules apply here).
      However, re-reading the requirement "capitalizing only the first letter of each word":
      This implies standard Title Case behavior where 'first' means the start of the string segment.
      If a word is already in mixed case like "hElLo", we want it to become "HEllo" or "Hello"? 
      Standard interpretation for this specific prompt usually implies converting to proper capitalization: First letter upper, rest lower? 
      OR just forcing first char upper and leaving the rest alone if they are part of a word.
      
      Let's interpret strictly as requested without over-engineering case conversion beyond what is necessary for 'capitalizing'.
      Usually "capitalize" implies making it uppercase/lowercase friendly. But to be safe on strict interpretation:
      We will take each word, and simply capitalize the first character (make it upper if lower) 
      while keeping the rest of the characters exactly as they are in the original string?
      
      Actually, standard utility behavior for "capitalize" often involves proper casing. 
      However, without explicit instruction to lowercase the rest, a safer bet is:
      Split by whitespace -> capitalize first char of each token join back.
      But wait, if input is "hello WORLD", result should be "Hello World"? Or "HELLO WORLD"?
      
      Let's assume standard Title Case logic where we ensure the first letter is Upper and subsequent letters are Lower? 
      No, the prompt says "capitalizing only the first letter". This phrasing suggests minimal alteration.
      But if I have a word like "abc", capitalizing the first makes it "Abc" (if rest stays same).
      
      However, most users expect "Hello World" from "hello world". 
      Let's look at the constraint: "capitalizing only the first letter of each word".
      If I do `word.capitalize()` in Python, it lowercases the rest. Is that allowed? 
      Usually yes, because you can't capitalize a 'z' without potentially affecting adjacent letters if not careful, but technically 'capitalize' is an operation on the string itself.
      
      Let's stick to the most robust interpretation: Make sure every word starts with Uppercase and subsequent chars are unchanged relative to their original state? 
      Or just apply standard `str.capitalize()` per word?
      Given the ambiguity, I will use a logic that ensures the first character is uppercase (if it was not already) and leaves everything else exactly as is. This strictly follows "only the first letter".
      
      Example: "hElLo" -> "HElLo"? No, usually we expect "Hello". 
      Let's reconsider standard English rules implied by such tasks. Usually, these scripts normalize case for readability unless specified otherwise.
      BUT the prompt says "capitalizing ONLY the first letter".
      If I change 'e' to lower in 'hEllo', am I capitalizing? No, that's normalizing.
      
      Decision: To be strictly compliant with "only", we capitalize the first char and leave the rest alone. 
      So "hello" -> "Hello", "HELLO" -> "HELLO". 
      Wait, if input is "hello", 'h' becomes 'H'. Result "Hello". Correct.
      If input is "HeLLo", result should be "HElLo"? That seems wrong for a utility tool intended to help users.
      
      Alternative interpretation: The user wants the output to look like proper sentence casing where words are titled, but perhaps they don't care about existing case inside? 
      Let's go with standard `capitalize()` per word because it is the functional equivalent of "capitalizing" in text processing contexts unless specified as a transformation.
      
      Actually, let's re-read carefully: "prints the result of capitalizing only the first letter".
      This could mean: Take the string, split into words, for each word set index 0 to Upper(), leave rest unchanged.
      Let's implement this strict version to avoid assumptions about lowercasing non-first letters which wasn't requested.
      
      Refined Logic:
      Split text -> list of words (stripped).
      For each word: if len > 0, char[0] = upper(char[0]), rest remains as is. Join with space.
      
      Wait, what about punctuation attached to words? "hello," -> "Hello,". 
      The split should handle whitespace primarily. Leading/trailing spaces preserved? Yes.
    """
    # Split by whitespace to identify word boundaries, but we need to preserve the original spacing structure if possible, or just treat as continuous text with variable length words separated by single spaces for simplicity in this context unless strict multi-space preservation is needed (usually not implied). 
    # Standard approach: split() removes multiple newlines/tabs. Let's use re.split('\s+') to handle complex whitespace and preserve it? Or simple join of split(' ') which collapses multiple spaces to one.
    # Given "command-line utility", collapsing extra spaces is usually acceptable unless specified otherwise, OR we should iterate the string directly.
    
    result = []
    i = 0
    n = len(text)
    current_word_start = None
    
    while i < n:
        char = text[i]
        
        # Check if it's a whitespace character (space, tab, newline)
        if ' \t\n\r' in chars or ord(char) <= ' ': 
            pass

if __name__ == '__main__':
    pass
