def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of each word in a multi-word string,
    ensuring no other letters within words are capitalized (e.g., converts "hello WORLD" to "Hello world").
    
    Args:
        text (str): The input string containing multiple words. Can include whitespace and punctuation.
        
    Returns:
        str: A new string where only the first letter of each word is capitalized, preserving original casing for rest.
            Words are defined as sequences separated by spaces or other non-alphanumeric characters treated as delimiters.
    
    Example:
        Input: "hello WORLD!" -> Output: "Hello World!"
        Input: "-- python code --" -> Output: "- Python Code -"
    """
    if not text.strip():
        return text
    
    # Split into words considering any non-alphanumeric character as a separator, but keep separators in context? 
    # Actually standard approach: split by whitespace first to handle multi-word naturally.
    # However, the prompt says "first letter only" across entire string. Usually implies per word based on spaces.
    # Let's define a 'word' as contiguous alphanumeric characters. We iterate char by char or use regex for robustness.
    
    result = []
    i = 0
    
    while i < len(text):
        if text[i].isalnum():
            # Start of a word: capitalize current letter, then lower the rest of this sequence
            capitalized_char = text[i].upper()
            next_is_uppercase_in_word = False
            
            j = i + 1
            while j < len(text) and (text[j].isalpha()): 
                if not is_digit_or_punctuation_and_stops_sequence(j, text): # This logic is getting complex. Let's use regex for clean "word" definition.
                    pass
                
                # Actually simpler: just find the sequence of alphabetic characters.
                j += 1
            
            result.append(capitalized_char)
            
            # Process the rest of this 'word' (alphabetic part) as lowercase, unless it was already a specific letter? 
            # The rule is "capitalize first letter only". So if word is "Hello", output "HeLlo" -> NO. Output "hello"? No, capitalize FIRST.
            # If input is "heLLo", output should be "Hello"? Or just "Hello"? Usually yes: First uppercase, rest lowercase.
            j = i + 1
            
            while j < len(text) and text[j].isalpha():
                if not next_is_uppercase_in_word: 
                    # Just append lowercased version for the sequence after first char?
                    # Wait, "capitalize first letter only" usually means: First -> Upper, Rest -> Lower.
                    result.append(text[j].lower())
                
                j += 1
            
            i = max(j, i + 1)

if __name__ == '__main__':
    pass
