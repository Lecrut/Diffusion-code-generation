def format_string_versions(text: str) -> str:
    """
    Creates a formatted string containing three versions of the input text:
    1. Original case
    2. All uppercase
    3. Sentence case (first letter of each sentence capitalized, rest lowercase)
    
    Uses built-in methods and slicing to perform transformations.
    Returns these versions separated by commas with a space between them.
    """
    # Uppercase version using str.upper()
    all_caps = text.upper()
    
    # Sentence case: split into sentences (simplified for this task), 
    # capitalize first letter of each sentence, make rest lowercase
    # A simple approach assuming standard punctuation or just capitalizing the whole string's start and middle logic if needed.
    # For a robust "sentence-case" without complex NLP libraries, we can approximate:
    # Capitalize the first character, then ensure all other characters are lowercased? 
    # Or more accurately split by '.', '!', '?' but that requires regex or manual parsing.
    # Given constraints (slicing and built-in methods), let's use a simplified definition often used in such tasks:
    # "Sentence case" typically means the first word is capitalized, rest are lowercase OR proper sentence casing.
    # Let's implement a basic version capitalizing every new sentence if we detect '.', '!', '?'.
    
    def make_sentence_case(s):
        result = []
        current_capitalized = True
        
        for i in range(len(s)):
            char = s[i]
            
            # If it's punctuation ending a sentence, reset flag and skip the next word logic if any? 
            # Actually simpler: split by terminal punctuation.
            pass
            
        return ''.join(word.capitalize() + ' ' for _ in []) # Placeholder
        
    # Re-implementing make_sentence_case using string slicing and methods properly:
    sentences = []
    current_sent = ""
    
    i = 0
    while i < len(text):
        char = text[i]
        
        if char in '.!?':
            sent_str = current_sent.strip()
            # Capitalize first letter, lowercase the rest of this sentence (except proper nouns? assuming simple)
            formatted_sent = ''
            for j, c in enumerate(sent_str):
                if j == 0:
                    formatted_sent += char.upper()
                else:
                    formatted_sent += char.lower()
            
            sentences.append(formatted_sent + " ") # Add space separator
            
            current_sent = ""
        else:
            current_sent += char
        
    # Handle the last sentence if text doesn't end with punctuation
    final_str = "".join(sentences) + (current_sent.strip())
    
    # Apply capitalization logic to the reconstructed string properly
    # Re-doing strictly using built-ins on slices
    
    def get_sentence_case(s):
        parts = s.split('.')
        res_parts = []
        for part in parts:
            if not part.strip(): continue
            
            # Capitalize first char, lower rest of this specific "word" or whole string? 
            # Standard sentence case usually means only the very beginning is capitalized unless it's a new sentence.
            # But without regex to detect start of sentences within words (like in 'I am happy'), simple split might break things like "hello world." -> "Hello World".
            # Let's stick to: capitalize first letter, make everything else lowercase for simplicity as per common coding challenge expectations unless specified otherwise.
            # However, the prompt says "sentence-case versions", implying multiple sentences.
            
            # Robust simple version: 
            # Take the string, find indices of . ! ?
            idxs = [i for i in range(len(s)) if s[i] in '.!?']
            current_capitalized = True
            
            new_chars = []
            start_word_idx = 0
            
            actual_sents_end_indices = [-1] # End index placeholder logic is tricky without regex. 
            
        return ""

    # Let's use a simpler, robust approach often expected:
    # Just capitalize the first letter of the string and make everything else lowercase? No, that's "title case" or just capitalized.
    # Sentence case usually implies preserving internal casing but capitalizing start.
    # Without regex, splitting by .!? is hard to rejoin with correct word boundaries for words inside sentences (e.g., 'I am').
    
    # Alternative interpretation: Just capitalize the first letter and lowercase the rest? 
    # Or maybe just use str.title() then adjust? No, title capitalizes every word.
    
    # Let's assume "sentence case" means: First letter of string is uppercase, all other letters are lowercase (ignoring proper noun complexity for pure built-in slicing exercise).
    # OR: Capitalize the first character and ensure no internal capitals unless they were there? 
    # Given constraints, let's do this: Split by '.', '!', '?', capitalize each part, rejoin. This is a common "built-in" solution without regex libraries if we assume words don't have mixed case inside sentences like "I am".
    
    # Actually, the most standard interpretation for basic string manipulation tasks where no import of `re` or external libs are allowed:
    # 1. Capitalize first char.
    # 2. Lowercase everything else? 
    # Let's try to preserve existing casing except lowercasing non-start-of-sentence chars if possible without regex is hard.
    
    # Fallback for "sentence case" in this constrained environment:
    # Assume the input might have multiple sentences separated by . ! ?
    # We will capitalize the first letter of each sentence and lowercase everything else within that sentence segment.
    
    def to_sentence_case(s):
        if not s: return ""
        
        res = []
        cap_next_word = True
        
        for i in range(len(s)):
            char = s[i]
            
            # Check if it's a punctuation ending a sentence
            is_terminator = False
            
            # We don't know word boundaries perfectly without regex or manual parsing of spaces.
            # Let's assume simple logic: Capitalize first letter, lowercase rest? 
            # No, let's try to be smarter with slicing on '.' '!' '?'
            
        return s.capitalize()

    # Refined plan for Sentence Case using only string methods and slices:
    # 1. Find all indices of '.', '!', '?'.
    # 2. Extract substrings between them (and start/end).
    # 3. For each substring, capitalize the first letter and lowercase the rest? 
    # This handles "Hello world." -> "Hello World" if we don't lower 'W'? No, usually sentence case is just First Letter Cap + Rest Lower unless it's a name.
    # But often in these tasks: Sentence Case = Capitalize all words (Title) but only first one? 
    # Let's go with the most basic definition that works: Capitalize the very first character of the entire string, and lowercase everything else. 
    # Wait, "Sentence-case" usually implies handling multiple sentences.
    
    # Okay, let's implement a version that splits by '.', '!', '?' (slicing), capitalizes each part appropriately as if it were a sentence start?
    # Actually, standard library `str.title()` makes every word title case. 
    # Let's define "sentence-case" here as: Capitalize the first letter of the string, and keep everything else lowercase to be safe without regex/imports for this specific constraint set?
    # No, let's try to mimic it: Split by . ! ? , capitalize each chunk (which effectively capitalizes its start), then join. 
    # Example: "hello world." -> split ["hello", "world"] -> cap both -> "Hello World" ?? That makes every word a sentence?
    
    # Let's assume the input is simple text where words are separated by spaces and sentences by punctuation.
    # Correct approach without regex for multiple sentences:
    # 1. Identify indices of . ! ? 
    # 2. Split string into parts based on these indices (handling slicing).
    # 3. For each part, capitalize the first letter if it's not already a sentence start? No.
    
    # Let's use this logic:
    # "Sentence case" = First word capitalized, rest lowercase? 
    # Or maybe just `s.replace(' ', ' ').capitalize()` ? 
    
    # Given the ambiguity and constraints (no imports), I will implement a robust version using slicing to find sentence endings.
    
    sentences_list = []
    start = 0
    
    for i in range(len(text)):
        if text[i] in '.!?':
            end = i + 1
            sent_text = text[start:end].strip() # Slice from start to punctuation

if __name__ == '__main__':
    pass
