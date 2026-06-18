def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to count occurrences of repeated letters (case-insensitive).
    
    Only letters that appear more than once in the original string are included as keys.
    Case is ignored during counting but preserved conceptually for uniqueness check; 
    however, based on standard interpretation unless specified otherwise ('a' and 'A'),
    we treat them as distinct characters to be safe, or combine if case-insensitivity was implied by context.
    
    Given the task says "letters that are repeated", typically this implies character identity regardless of case in natural language tasks, 
    but strictly speaking in programming strings 'a' != 'A'. To provide a robust solution often expected:
    We will treat them as distinct unless specified to lower-case first. However, usually such problems expect case-insensitivity for "letters".
    
    Let's assume case-sensitive based on raw string processing unless context implies otherwise. 
    But if the user meant case-insensitive (common in word frequency tasks), we should probably normalize.
    
    Re-reading: "keys are the letters that are repeated" -> 'a' and 'A' as different letters? Usually yes, they are different characters.
    Example: "aabBCc" -> {'a': 2, 'b': 1 (not included), 'B': 0...} wait B appears once. 
    Actually in "aabBCc": a->2, b->1, B->1, c->2. Repeated only if count > 1.
    
    However, to be most useful and common interpretation of "letters" without explicit case instruction:
    We will perform case-sensitive counting first as that is the default for string operations unless told otherwise.
    
    Wait, let's look at standard behavior for such prompts. If I have "Aa", are A repeated? Only if we consider them same letter.
    Let's implement case-insensitive to be helpful, but map back to original casing or lowercase keys? 
    The prompt asks for keys as letters. Lowercase is safer for dictionary lookup of 'letters'.
    
    Decision: We will count based on lowercased characters to treat 'A' and 'a' as the same letter type, 
    outputting counts in a case-insensitive manner (keys stored as lowercase). This handles "repeated letters" naturally.
    """
    char_counts = {}
    
    # Normalize input: convert all to lowercase for uniform processing of "letters"
    normalized_string = s.lower()
    
    for char in normalized_string:
        if not char.isalpha():  # Only process alphabetic characters (ignore numbers/symbols)
            continue
        
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Filter to only include letters that are repeated (count > 1)
    result = {letter: count for letter, count in char_counts.items() if count > 1}
    
    return result

if __name__ == '__main__':
    # Sample string with multiple repeated letters and some unique ones.
    sample_input = "Hello World!"
    output_dict = process_string(sample_input)
    print(output_dict)