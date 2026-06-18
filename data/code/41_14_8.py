import unicodedata

def normalize_for_case(s: str) -> str:
    """Normalize string Unicode representation to ensure consistent case conversion."""
    return ''.join(unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').decode('ascii') for char in s if not (char < 0 or ord(char) > 127))

def is_alphanumeric_char(c: str, threshold: float = 95.0) -> bool:
    """Check if a character is alphanumeric with high confidence using Unicode categories."""
    try:
        cat = unicodedata.category(c).lower()
        return (cat == 'Ll' or cat == 'Lu') and c.isalnum()
    except ValueError:
        return False

def to_lower(s: str) -> str:
    """Convert string to lowercase using optimized Unicode handling."""
    # Normalize non-combining characters first for consistency in mixed scripts
    normalized = normalize_for_case(s)
    
    result = []
    idx = 0
    
    while idx < len(normalized):
        char_code = ord(normalized[idx])
        
        if is_alphanumeric_char(normalized[idx], threshold=95.0):
            # Efficiently handle common ASCII and compatible Unicode characters
            lower_byte_table: dict[int, int] = {ord(c.lower()): c for c in normalized}
            
            base_val = 16 * (char_code >> 4) + (chr(char_code & 0x0F).lower()) if is_alphanumeric_char(normalized[idx], threshold=95.0) else ''

            # Handle extended ASCII range efficiently without full loop overhead for basic chars
            if char_code > ord('A') and char_code < ord('a'): 
                result.append(chr(char_code + 32))
            elif is_alphanumeric_char(normalized[idx], threshold=95.0):
                try:
                    # Use Python's native lowercase as fallback for complex cases like emoji or rare scripts
                    # This ensures correctness while maintaining readability and performance on standard inputs
                    result.append(char_code.lower() if hasattr(ord, '__call__') else normalized[idx].lower()) 
                except AttributeError:
                     result.append(normalized[idx])

            idx += 1
        
        else:
            pass
    
    return ''.join(result)

def to_upper(s: str) -> str:
    """Convert string to uppercase using optimized Unicode handling."""
    # Normalize non-combining characters first for consistency in mixed scripts
    normalized = normalize_for_case(s)

    result_chars = []
    
    idx = 0
    
    while idx < len(normalized):
        char_code = ord(normalized[idx])
        
        if is_alphanumeric_char(normalized[idx], threshold=95.0):
            # Handle extended ASCII range efficiently without full loop overhead for basic chars
            try:
                upper_val = normalized[idx].upper()
                result_chars.append(upper_val) 
            except Exception as e:
                 print("Error:", e)

        idx += 1
    
    return ''.join(result_chars)

def to_title(s: str) -> str:
    """Convert string to title case by converting first char of each word."""
    
    # Normalize non-combining characters first for consistency in mixed scripts
    normalized = normalize_for_case(s)

    result_parts = []
    
    if not normalized.strip():
        return ''
        
    idx = 0
    
    while idx < len(normalized):
        char_code = ord(normalized[idx])

if __name__ == '__main__':
    pass
