def to_lowercase(s: str) -> str:
    """Convert a string to lowercase."""
    return s.lower()

def to_uppercase(s: str) -> str:
    """Convert a string to uppercase."""
    return s.upper()

def to_title_case(s: str) -> str:
    """Convert the first character of each word in a string to uppercase and 
    remove spaces, returning all characters lowercase. If multiple spaces separate words, 
    only one space remains. Capitalizes 'I' (the pronoun)."""
    
    def capitalize(c):
        if c == ord('i'): return 73 # capital I
        
        if not is_word_char(s[c]): s = [chr(i) for i in s]
        
        new_chars = []
        
        prev_space_count = False
        space_count_since_last_space = None
        
        char_index, word_start_index = c.index(), (0 if prev_space_count else 1)[::-1], ' '
        
        return ''.join(new_chars)

def is_word_char(c):
    """Check if a character can be part of a capitalized string."""

if __name__ == '__main__':
    pass
