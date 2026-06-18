import sys

def capitalize_first_of_each_word(text: str) -> str:
    """
    Capitalizes only the first letter of each word in the input text.
    Words are separated by one or more whitespace characters.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized,
             and all other lowercase letters preserved as per original casing 
             except for being lowercased after capitalization if needed? 
             
       Correction based on "capitalizing only the first letter":
       This means: First char -> uppercase. Rest of chars in that word -> keep original case or lower?
       
       Usually, such tasks imply: Title Case behavior but strictly 'only' first letter capitalized.
       Let's assume standard interpretation: 
         - Take input "hello WORLD". Output should be "Hello World" (first letters cap).
         
       If the requirement is strict literal capitalization of just index 0 and rest unchanged?
       Or does it imply converting to title case style where non-first are lowercased?
       
       Let's re-read: "capitalizing only the first letter". 
       This implies we touch ONLY the first letter. The rest stays as they were originally in terms of casing,
       OR maybe the instruction implies standard Title Case logic (rest become lowercase).
       
       However, often these prompts mean: Make it look like a proper sentence where each word starts with cap.
       Let's assume the safest interpretation for "capitalizing": 
         - First char -> upper()
         - Rest of chars in word -> lower()? Or leave alone?
         
       If I have "HeLLo", and only capitalize first letter -> "HElLo"? No, that doesn't sound like capitalization.
       Usually it means: Convert the whole string to title case logic but strictly one change per word start.
       
       Let's look at common edge cases for this prompt type. 
       If input is "a b C d". Output should be "A B C D" (rest lowercased) or "A b c D"?
       
       Given the phrasing "capitalizing only", it suggests minimal change to make caps happen.
       But typically, a utility doing this would normalize rest of word to lowercase too? 
       Actually, let's look at similar problems. Often they want: "The Python Way".
       
       Let's assume standard Title Case behavior where non-first letters are lowercased if not already upper?
       No, the prompt says "only the first letter... in each word". This implies NO change to other letters.
       So "HeLLo" -> "HELlO"? That seems wrong for a utility named capitalizing. 
       
       Let's try: Input "hello world" -> Output "Hello World". (Rest lowercased).
       Why? Because you can't capitalize the first letter of 'world' if it starts with lowercase, unless you assume input is mixed case and we want Title Case.
       
       Wait, strict reading: 
         - Find words by whitespace split.
         - For each word string S: result_word = S[0].upper() + S[1:] (unchanged).
         
       Let's test this hypothesis against "hello world". Result: "Hello World". Correct.
       Against "HeLLo WoRLd": 
           Option A (Strict): "HELlO WorLd" -> First char cap, rest unchanged.
           Option B (Title Case logic): "Hello Word" -> Cap first, lower rest.
           
       The phrase "capitalizing only the first letter" strongly hints at Option A: Do nothing to other letters except ensuring they are what they were? 
       Actually, if I say "capitalize this word", and you give me "hello", I make it "Hello". If I have "HeLLo", do I make it "HELlO"? That's weird.
       
       Let's assume the most common utility expectation: Title Case but strictly one letter change per word? 
       Actually, let's go with Option A (Strict) because of the word "only". 
       If they wanted title case, they would say "Convert to title case" or "Capitalize each word".
       "Capitalizing only the first letter" implies touching exactly that character.
       
       So: Split text by whitespace -> For each part w: return [w[0].upper() + w[1:] if len(w) > 1 else "" for x in parts] joined back? 
       Wait, preserving internal spacing is important too (multiple spaces).
       
    """
    # Handle empty string
    if not text:
        return ""
    
    result_parts = []
    
    # Split by one or more whitespace to preserve leading/trailing/multiple whitespaces structure roughly?
    # Actually standard split() removes all whitespace. We need re.split or regex to keep spaces, OR iterate chars manually.
    
    # Approach: Iterate char by char, detect start of word (non-alphanumeric before a letter?) 
    # Or just use re.findall with capture groups for words and separators? 
    # Simpler: Use split(' ') but that collapses multiple spaces if not careful? No " ".split(" ") keeps empty strings.
    
    # Let's use regex to separate non-word characters from word start/end to preserve formatting exactly.
    import re
    
    # Pattern to match words (sequences of letters/numbers) and everything else as separators, keeping structure.
    # Actually simpler: Replace all whitespace with a unique placeholder? No.
    
    # Let's iterate manually for precision on spacing.
    current_word = []
    is_first_char_of_new_word = False
    
    text_list = list(text)
    
    def capitalize_char(c):
        if c.isalpha():
            return c.upper()
        else:
            return c
            
    # Strategy 1: 
    # Split into tokens where a token starts with an uppercase letter or is the start of string? No.
    # A word starts when we encounter a sequence of letters/numbers after non-letters (or at index 0).
    
    def process_text(s):
        output = []
        n = len(s)
        
        for i in range(n):
            char = s[i]
            
            if not char.isalnum(): # Non-alphanumeric acts as a space/separator
                is_first_char_of_new_word = False
                output.append(char)
            elif is_first_char_of_new_word and char.isalpha():
                # Capitalize this letter, reset flag for next word part? 
                # Wait, we just capitalized the first. The rest of alphanumerics in current word are NOT changed per strict reading.
                # But what defines "end" of a word if it contains numbers? Usually alphanumeric sequence is one word.
                
                output.append(char.upper())
            elif char.isalpha() and not is_first_char_of_new_word:
                # Middle or end part of current word -> unchanged (per strict reading)
                output.append(char)
            
            else:
                # Check if we are starting a new sequence of alphanumerics? 
                # We need to detect start of alphanumeric run.
                pass
                
        return "".join(output)
    
    # Refined Logic:
    # Detect when current char starts an alphanumeric block that follows non-alphanumeric or is at index 0 and followed by alpha/num?
    # Actually, just check if s[i-1] was NOT alphanum (or i==0). If so, and s[i] IS alphanum -> This might be start. 
    # But we only capitalize FIRST LETTER of WORD. So first ALPHABETICAL letter in the word?
    # Or is it any alphanumeric run considered a "word"? Usually words are alphabetic sequences.
    
    # Let's assume standard definition: A word is a contiguous sequence of letters (a-z, A-Z). 
    # But what about numbers? e.g., "abc123". Is '1' part of the first letter? No, only 'first LETTER'. 
    # So if input is "abc 123 def", words are ["abc", "def"]. What about "ab c"?
    
    # Let's stick to simplest interpretation: Split by whitespace -> Capitalize index 0. Keep rest exactly as is.
    # But wait, if I have two spaces? "a   b". split() gives ['a', 'b']. Join with multiple spaces lost. 
    # Must preserve original spacing.
    
    # Re-doing loop logic correctly:
    output_list = []
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]

if __name__ == '__main__':
    pass
