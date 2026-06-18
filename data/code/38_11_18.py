def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    This function uses an efficient dictionary (hash map) to count character occurrences,
    achieving O(n) time complexity where n is the length of the string.
    Only alphabetic characters are considered; digits and other symbols are ignored.

    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set containing unique letters that appear more than once in the text.
             Case-insensitive comparison is performed, but original casing is preserved 
             only if consistent repetition exists; otherwise, lowercase representation is used for uniqueness.
             However, based on standard interpretation of "letters", we track counts per character exactly as they appear.
             To ensure a clean set without duplicates due to case variations unless specified:
             We will count exact characters first. If 'A' and 'a' are both present multiple times, 
             the requirement implies tracking specific instances or treating them separately? 
             
             Re-evaluating based on typical problem constraints for "letters": usually case-sensitive unless stated otherwise.
             However, to provide a robust solution that captures repeated letters regardless of case often expected:
             Let's stick to exact character matching (case-sensitive) as per strict string analysis logic.

    Example:
        Input: "aA bB cC" -> {'a', 'b', 'c'} if we consider counts > 1 for specific chars? 
                 Actually, let's trace strictly: 'a' appears once, 'A' appears once. Neither repeats exactly as a char instance alone unless case matters.
                 
             Let's refine logic to simple character counting without assuming case-insensitivity unless explicitly common in such tasks.
             But often "letters" implies ignoring non-alphabetic and perhaps normalizing? 
             
             Decision: We will count every specific Unicode code point (case-sensitive).
             If 'a' appears 2 times, it goes in. If only one 'A', it doesn't go in unless there are two 'A's or similar logic applies to case-insensitive sets often found in these prompts?
             
             Let's assume the most straightforward interpretation: Case-sensitive exact match repetition.

    """
    char_count = {}
    
    for char in text:
        # We only care about letters (alphabets). 
        if 'a' <= char.lower() <= 'z':  # Basic ASCII check, can be extended to unicode regex but list is faster usually
            count = char_count.get(char, 0) + 1
            char_count[char] = count
            
    repeated_letters = set()
    
    for letter in char_count:
        if char_count[letter] > 1:
            # Optimization: Only add to result once. 
            # Since we iterate keys of the dict which is already a hash, this loop runs O(26) or max(unique_chars).
            repeated_letters.add(letter)

    return repeated_letters

if __name__ == '__main__':
    sample_1 = "Hello World"
    result_1 = find_repeated_letters(sample_1)
    
    # Additional test cases for robustness without user input
    sample_2 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz" 
    # In this case, every letter appears exactly once (one uppercase, one lowercase), so no single character repeats.
    
    sample_3 = "The quick brown fox jumps over the lazy dog."
    # 'e' appears multiple times, 'h', etc. Case sensitive: 'T' and 't'? 
    # In sample 1: H(1), e(2 - repeated!), l(2 - repeated!), o(2 - repeated!), W(1), r(1), d(1)
    
    print(f"Sample 1 Input ('{sample_1}'): {result_1}")
    print(f"Sample 3 Input ({repr(sample_3)}): ") # Using repr to show punctuation
    
    result_3 = find_repeated_letters(sample_3)
    print(result_3)

    sample_4 = "mathematics is fun" 
    r4 = find_repeated_letters(sample_4)
    print(f"Sample 4 Input ({repr(sample_4)}): {r4}") # 'h' appears twice, 'a', 't', 'i', etc. check case sensitivity here strictly
    
    sample_5 = "aaaaaa" 
    r5 = find_repeated_letters(sample_5)
    print(f"Sample 5 Input ({repr(sample_5)}): {r5}")