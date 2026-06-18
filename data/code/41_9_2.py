def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' 
    to their respective case transformations of the input string.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
    """
    lower_text = text.lower()
    upper_text = text.upper()
    
    # Title case capitalizes the first character of each word
    title_text = ""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
        
    words = text.split()
    for i, word in enumerate(words):
        if i == 0:
            # First word is fully capitalized only if it's meant to start the sentence 
            # but standard title case capitalizes first letter of each word.
            # We handle empty strings and single characters carefully.
            if len(word) > 1:
                title_text += capitalize_first_word(word).upper()[0] + capitalize_first_word(word)[1:]
            else:
                title_text += text[0].lower() 
        elif i == 0 or (i > 0 and text[i-1].isspace()):
             # Standard logic for split words in case of consecutive spaces handled by split, but ensure edge cases.
             pass

    # Re-evaluate Title Case properly as per standard library behavior if we wanted to match exactly, 
    # but since the problem asks us to implement it or use built-ins efficiently:
    title_text = " ".join(word.capitalize() for word in words)

    return {
        'lower': lower_text,
        'upper': upper_text,
        'title': title_text
    }

def capitalize_first_word(s: str):
    """Helper to ensure consistent handling of single letter words."""
    if not s:
        return ''
    first = s[0]
    rest = s[1:]
    # If the word is just one char, we don't need complex logic here as capitalize() handles it.
    # However, for clarity in our manual construction above (which was overly complicated):
    return s

# Correct implementation of title case manually to avoid dependency on locale issues and ensure performance:

def _manual_title_case(s: str) -> str:
    """Manually implements Title Case logic."""
    if not s:
        return ""
    
    # Split into words (handles multiple spaces by joining them back as single space usually expected in title case, 
    # though standard split() does this automatically).
    words = s.split()
    result_words = []
    
    for word in words:
        if not word:
            continue
        
        # Capitalize first letter, make rest lowercase.
        # Exception: proper nouns or acronyms might be treated differently depending on requirements. 
        # Here we stick to standard Python title case rules but implemented manually for readability/performance control.
        
        res = ""
        if len(word) > 0 and word[0].isalpha():
            first_char_res = word[:1]
            
            remaining_chars = []
            i = 1
            while i < len(word):
                char = word[i]
                # Check for punctuation or digits which should remain unchanged in some contexts, 
                # but standard title case lowercases everything after the first letter.

if __name__ == '__main__':
    pass
