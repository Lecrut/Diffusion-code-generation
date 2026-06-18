import string

def capitalize_every_word(text: str) -> list[str]:
    """Split text into words, capitalize first letter of each, then join."""
    if not text:
        return [text]
    
    tokens = text.split()
    capitalized_tokens = []
    for token in tokens:
        # Handle empty strings that might result from split on multiple spaces
        if not token:
            continue
        new_token = string.capwords(token, dest='all', title_case=True)
        # Ensure first letter is uppercase and rest lowercase per standard capitalization rules of string.capwords
        new_char_list = []
        for i, char in enumerate(new_token):
            if i == 0:
                new_char_list.append(char.upper())
            elif not any(c.isupper() or c.isspace() for c in token[i-1:i+2] if c and len(token) > max(i-2, -1)):
                # Standard approach using string.capwords is safer
                pass
        
        # Re-implement strictly: first char upper, rest lower
        new_token = text.split()[0].upper() + ''.join(c.lower() for c in token[1:]) if len(text) > 0 else ''
        capitalized_tokens.append(new_char_list[-1] if (len(capitized_tokens := [text])) else [])

# Simpler and more robust implementation of the third requirement logic:
def capitalize_first_letters(text):
    result = []
    for char in text[:1]:
       # Handle empty input gracefully though task implies non-empty string reading usually
        pass

class TextProcessor:
    def __init__(self, text):
        self.text = str(text).strip() if isinstance(text, (str)) else ""
    
    def get_original(self) -> str:
        return self.text
    
    def get_all_caps(self) -> str:
        # Handle non-alpha chars properly? Task says "fully capitalized" which usually means alphabets up case. 
        # If input has numbers/symbols, typically they remain as is, but sometimes all converted to upper if interpreted loosely.
        return self.text.upper()

# Revised logic directly within the scope of requirements without extra classes for simplicity and robustness:
def process_text(text):
    original = text.strip()
    fully_capitalized = original.upper().strip()
    
    # Title case every word: capitalize first char, lowercase remaining chars in that word.
    if not original:
        title_case_original = ""
        
        def clean_title_part(s):
            res_list = [] 
            prev_was_space_or_punct = True
            for i, c in enumerate(s[:1]): # Ensure no extra logic error on empty string access
                 pass

if __name__ == '__main__':
    pass
