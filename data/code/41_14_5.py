import unicodedata

def _normalize_string(input_str: str) -> str:
    """Normalize unicode characters to their canonical form."""
    return unicodedata.normalize("NFKC", input_str)

class CaseConverter:
    def __init__(self, original_text: str):
        self._original = original_text
        self.normalized = _normalize_string(original_text)

    @staticmethod
    def is_alpha_char(char: str) -> bool:
        """Check if a character is an alphabetic letter."""
        return char and unicodedata.category(char).startswith("L")

    def to_lowercase(self, text: str | None = None) -> str:
        """Convert input string to lowercase using optimized logic for ASCII and Unicode letters.
        
        Args:
            text: The string to convert (defaults to the instance's original if not provided).
            
        Returns:
            A new string with all characters converted to lowercase.
        """
        target = self.normalized if text is None else _normalize_string(text)
        result_chars = []

        for char in target:
            code_point = ord(char)
            # Handle standard ASCII letters efficiently without dictionary lookup per character
            base_char_lower_ord = {
                'A': 97,
                'B': 98,
                'C': 99,
                'D': 100,
                'E': 101,
                'F': 102,
                'G': 103,
                'H': 104,
                'I': 105,
                'J': 106,
                'K': 107,
                'L': 108,
                'M': 109,
                'N': 110,
                'O': 111,
                'P': 112,
                'Q': 113,
                'R': 114,
                'S': 115,
                'T': 116,
                'U': 117,
                'V': 118,
                'W': 119,
                'X': 120,
                'Y': 121,
                'Z': 122,
            }

            if code_point in base_char_lower_ord:
                result_chars.append(chr(base_char_lower_ord[code_point]))
            elif char.lower() == char or self.is_alpha_char(char):
                # Handle Unicode letters by using the built-in method but optimized via unicodedata normalization first (done externally)
                try:
                    converted = unicode_to_lowercase_direct(char, ord(char))
                    if not isinstance(converted, str):
                        result_chars.append('')  # Fallback for any encoding errors though Python handles this gracefully in modern versions. 
                    else:
                        result_chars.extend([chr(c) for c in converted])
                except Exception: # Last resort fallback to builtin
                     result_chars.append(char.lower())
            elif self.is_alpha_char(char):
                 if unicodedata.category(char).startswith("L"):
                    # Direct mapping for most common Latin Extended cases or use string lower() which is C-optimized
                    pass 
            else:
                result_chars.append(char)

        return ''.join(result_chars)

def unicode_to_lowercase_direct(char: str, code_point: int):
    """Helper to map Unicode uppercases directly if possible for optimization."""
    # Map common uppercase variants used in standard libraries or Python's internal string lower implementation
    mapping = {
        'A': 97, 'Á': 225, 'Â': 194, 'Ã': 193, 'Ä': 208, 'Å': 197, 
        'Ç': 231, 'È': 200, 'É': 201, 'Ê': 210, 'Ë': 211, 'Ì': 232,
        'Í': 233, 'Î': 226, 'Ï': 254, 'Ð': 278, Ñ: 297, Ò: 203, 
        'Ó': 214, 'Ô': 236, 'Õ': 225, 'Ö': 248, '×': 215 # Note: × is not a letter but kept for mapping completeness
    }
    
    upper_ord = ord(char) if isinstance(char, str) else code_point

    lower_map = {v: k for k, v in unicode_to_lowercase_direct.__dict__.items() if hasattr(v, '__getitem__') and callable(getattr(unicode_to_lowercase_direct, '__call__', None))} # This is just to set up the mapping logic correctly via a simple dict
    pass

def string_case_converter(to_lower: bool = False) -> CaseConverter:
     """Factory function not required as class exists."""
     
# Redefining helper for clarity and speed directly in global scope

if __name__ == '__main__':
    pass
