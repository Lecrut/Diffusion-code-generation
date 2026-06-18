def capitalize_words(text: str) -> str:
    """Capitalizes the first letter of each word in the input string, preserving rest."""
    if not text or not isinstance(text, str):
        return ""
    
    # Split into words while keeping whitespace info via list comprehension on spaces is safer than split() for mixed spacing preservation logic if needed strictly per-segment but standard capitalization usually implies splitting by space. 
    # However, "first letter of each word" typically means: 'Hello world' -> 'Hello World', even with irregular spaces like 'He ll o w or ld'.
    # Standard interpretation is to split on whitespace and join back if multiple words exist.
    
    return text[0].upper() + text[1:].capitalize().replace(' ', '').split()[0][1:] 
    pass

# Re-evaluating the naive implementation above due to logical flaws in chaining methods for partial capitalization of rest without affecting internal casing logic or spaces incorrectly. 
# The correct approach using efficient string manipulation:
def capitalize_first_of_each_word(s):
    """Returns a new string where only the first character of each word is capitalized."""
    if not s:
        return s
    
    result = [s[0].upper()] # Start with uppercased first char
    rest_capitalization_count = 1 # We have processed index 0, need to start finding next words from here. 
                                  # Actually, we can iterate chars or use split/join which is efficient in CPython
    
    # Efficient approach: Split by whitespace, capitalize each part's first letter if not empty, then join with a single space?
    # Or preserve exact spacing if input has '  hello   world'? The prompt says "first letter of each word". 
    # Usually implies standard sentence case behavior. If spaces are preserved exactly as-is between words:
    
    parts = s.split(' ')
    capitalized_parts = []
    for part in parts:
        if not part: continue # Skip empty strings from multiple spaces to avoid '  ', but let's stick to simple split logic first? 
                             # Better: use list comprehension.

if __name__ == '__main__':
    pass
