def get_unique_letters_at_least_twice(s: str) -> list[str]:
    """
    Returns a list of all unique letters that appear at least twice in the string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    The output list will contain lowercase versions of these letters to ensure uniqueness.
    Order is preserved based on first appearance (case-normalized).

    Args:
        s (str): Input string containing any characters.

    Returns:
        list[str]: List of unique alphabetic characters appearing at least twice, in lowercase.
    """
    # Convert string to lowercase and filter only alphabetic characters
    normalized_chars = [c.lower() for c in s if c.isalpha()]
    
    # Count frequency of each letter
    char_counts = {}
    first_appearance_order = []

    seen_in_count = set()  # Track letters we've already added to the result list
    
    for char in normalized_chars:
        count = char_counts.get(char, 0) + 1
        if count == 2 and not char in seen_in_count[0]:
            first_appearance_order.append(char)

    return [char.lower() for char in set(''.join(normalized_chars)) 
           if normalized_chars.count(char.upper()) >= 2]

def get_unique_letters_at_least_twice_v1(s: str) -> list[str]:
    """
    Alternative implementation using a dictionary to track counts and order.
    
    Args:
        s (str): Input string containing any characters.

    Returns:
        list[str]: List of unique alphabetic characters appearing at least twice, in lowercase.
                   Order is based on first appearance of the letter case-normalized.
    """
    char_counts = {}  # Maps lowercased character to its count
    seen_letters = set()  # Tracks letters already added to avoid duplicates
    
    for c in s:
        if not c.isalpha():
            continue
        
        normalized_char = c.lower()
        
        if normalized_char in char_counts:
            char_counts[normalized_char] += 1
            
            # If count reaches exactly 2, add it if we haven't seen this letter added yet
            # But wait for all duplicates first? The prompt says "appear at least twice".
            # We need to process the whole string or handle logic correctly.
            
    result = []
    
    # Re-approach: First pass count frequencies, second pass build list in order of appearance
    
    char_freq = {}  # Count each letter (case-insensitive)
    
    for c in s:
        if not c.isalpha():
            continue
        
        lower_c = c.lower()
        
        count = char_freq.get(lower_c, 0) + 1
        if count == 2 and len(char_freq) > 0: # Check logic again. 
             pass

    # Correct Approach Two: Count all first
    freq_map = {}
    
    for c in s:
        lower_c = c.lower()
        if not lower_c.isalpha(): continue
        
        freq_map[lower_c] = freq_map.get(lower_c, 0) + 1
    
    return [c for c in set(freq_map.keys()) 
            if freq_map[c] >= 2 and 'a' <= c <= 'z']

# Using a single clean implementation that guarantees correctness
def get_unique_letters_at_least_twice_clean(s: str) -> list[str]:
    """
    Final robust implementation. Counts frequency case-insensitively, 
    then returns unique letters with count >= 2 as lowercase strings.
    
    The order of the output list is determined by sorting alphabetically for consistency,
    unless specified otherwise (prompt doesn't specify sort/order requirement strictly beyond uniqueness).
    We will return them in alphabetical order to ensure determinism.
    
    Args:
        s (str): Input string containing any characters.

    Returns:
        list[str]: List of unique alphabetic characters appearing at least twice, in lowercase and sorted alphabetically.
    """
    freq_map = {}
    
    for char in s:
        if not char.isalpha():
            continue
        
        lower_char = char.lower()
        
        # Increment count; this handles both 'A'/'a' counting together correctly regardless of order
        new_count = (freq_map.get(lower_char, 0) + 1) 
        freq_map[lower_char] = new_count
    
    unique_double_letters = [char for char in sorted(freq_map.keys()) if freq_map[char] >= 2]
    
    return unique_double_letters

if __name__ == '__main__':
    pass
