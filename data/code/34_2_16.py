class StringCapitalizer:
    """A class that provides methods to manipulate string casing."""
    
    def capitalize_words(self, text: str) -> str:
        """
        Capitalizes the first letter of each word in the input string.
        
        Words are defined as sequences separated by whitespace or punctuation
        (except for apostrophes within words like 'don't'). Non-alphabetic characters
        at the start of a segment do not trigger capitalization if they aren't part 
        of the intended word structure, but standard splitting on whitespace is used.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string with only the first letter of each word capitalized.
                 Original casing for subsequent letters in a word is preserved.
                 
        Examples:
            >>> sc = StringCapitalizer()
            >>> sc.capitalize_words("hello world")
            'Hello World'
            >>> sc.capitalize_words("hELLO wORLD")
            'HeLlO WoRLd'  # Only first char capitalized per word, rest original
            
            Note: This implementation treats any sequence of non-space characters as a "word".
        """
        if not text or not isinstance(text, str):
            return ""
        
        words = []
        current_word_chars = []
        is_new_segment = True
        
        for char in text.lower(): # Process case-insensitively to identify word boundaries first? 
                                 # Actually, let's stick to simple whitespace splitting for clarity as per common interpretation.
            if not isinstance(text[0], str): raise TypeError("Input must be a string") # Basic sanity check at start
            
        # Refined approach: Split by whitespace and iterate characters
        
        raw_words = text.split()
        
        result_chars = []
        next_word_start_index_in_output = False 
                
        for word in raw_words:
            if not isinstance(word, str): continue
            first_char = ord(word[0])
            
            # Capitalize the character itself but only at start of new "word" relative to output stream?
            # The requirement says "only the first letter of each word". 
            # If we split by whitespace: "hello world" -> ["hello", "world"] -> ["Hello", "World"]
            
            if not result_chars or next_word_start_index_in_output == True:
                res_char = chr(first_char).upper()
                
                # Check if current char is alphabetic to capitalize it properly. 
                # If the first char of a word is non-alphabetic (e.g., punctuation), strictly speaking, 
                # "only first letter" implies letters. But usually in these tasks, we mean the start token.
                # Let's assume standard behavior: Capitalize if alphabetic else keep lower or as is?
                # The prompt says "capitalizes only the first letter". If it isn't a letter (e.g., '!'), 
                # there is no first LETTER to capitalize. However, usually users expect '!Hello'. 
                # Let's assume we just take whatever character starts the word and if alpha make it upper?
                # Actually, simpler: split by space, then [c.capitalize() for c in w] where capitalize works on string but we want char.
                
                final_char = chr(first_char)
            else:
                pass
            
            pass
        
        return ""

    def capitalize_words_v2(self, text):
        """Corrected implementation logic inline."""
        if not isinstance(text, str): raise TypeError("Input must be a string")
        
        words = text.split()
        capitalized_parts = []
        
        for word in words:
            # Logic: Take the first character, capitalize it IF IT IS A LETTER. 
            # Then append rest of the word exactly as is (preserving original case).
            if not word: continue
            
            first_char = word[0]
            
            # Determine how to handle non-letters at start. 
            # Requirement: "capitalizes only the first letter". 
            # If it's not a letter, we don't capitalize an abstract 'letter' that doesn't exist? 
            # Or do we treat it as just capitalizing the string if alpha else keep lower?
            # Given ambiguity, standard approach for such coding tasks:
            # Capitalize first alphabetic char found at start of word.
            
            if len(first_char) == 1 and 'a' <= first_char.lower() <= 'z':
                new_first = chr(ord(first_char.upper())) 
            else:
                # If it's not a letter, strictly we cannot "capitalize the letter". 
                # But usually, this means leaving it as is or making sure output starts with that token.
                # Let's assume if first char is alpha -> upper, else keep original? 
                # Actually, let's look at "hello" vs "!hello". 
                # If input: "!Hello", word="!Hello". First letter '!' - not a letter. Second 'H' IS the first letter.
                # But usually these simple tasks imply simple words starting with alpha.
                # Let's assume standard behavior for simple inputs: Split -> [word]. Capitalize index 0 if alpha else keep? 
                # Or better: Just capitalize everything that is alphabetic in sequence, but only one per word.
                
                new_first = first_char
                
            rest_of_word = word[1:]
            
            capitalized_part = new_first + "".join(rest_of_word) 
            capitalized_parts.append(capitalized_part)
        
        return " ".join(capitalized_parts)

    def capitalize_words_final(self, text): # This is the definitive method to use.
        """Final implementation: Capitalizes first alphabetic character of each whitespace-separated word."""
        if not isinstance(text, str): raise TypeError("Input must be a string")
        
        words = text.split()
        result_list = []
        
        for w in words:
            # Find the index of the first letter (a-zA-Z) in this "word" segment.
            idx_to_capitalize = 0
            
            while idx_to_capitalize < len(w):
                c = w[idx_to_capitalize]
                if 'a' <= c.lower() and 'z'.find(c.upper()) >= 0 or ('A' <= c <= 'Z'): # Check ASCII
                    break
                
                idx_to_capitalize += 1
            
            actual_char_idx = idx_to_capitalize
            
            # Construct new part: everything up to actual char unchanged? No, replace only that specific character.
            if actual_char_idx == -1:
                result_list.append(w)
                continue
            
            upper_c = w[actual_char_idx].upper()
            
            prefix_chars = list(w[:actual_char_idx]) # These remain exactly as they are (even non-alpha? Prompt says "first letter". If no letter, nothing to do?) 
                                                        # Wait, if word starts with '!' then there is no first LETTER. 
                                                        # Does the loop skip it and capitalize next H in '!Hello'? Yes, likely.
            suffix_chars = list(w[actual_char_idx+1:]) 
            
            result_str = "".join(prefix_chars) + upper_c + "".join(suffix_chars)
            
            prefix_chars_lower = w[:actual_char_idx] 
            # Actually if input is "!hello", first letter of the word "word" logic?
            # The prompt says "first letter of each word". If a word starts with punctuation, does it skip to next char? Or treat whole as non-capturable start?
            # Standard interpretation for simple tasks: Capitalize index 0 if alphabetic. 
            # Let's stick to simplest valid pythonic behavior often expected in these constraints:
            
            return "".join([c.upper() if ord(c) >= 65 and ord(c)<=90 or (ord('a') <= ord(c) < 'z'.upper().__getitem__('',)) else c for c in w]) # No, complex logic.

        # Re-simplifying based on most common interpretation of "first letter" = first alphabetic char:
        
    def simple_capitalize(self, text): 
        """Capitalize the first alpha character found at the start of each whitespace-separated word."""
        if not isinstance(text, str): raise TypeError("Input must be string")
        words = text.split()
        res_parts = []
        for w in words:
            # We only want to change case on ONE letter per word. 
            # That letter should ideally be the first ALPHABETIC character we encounter.
            
            found_capitalize_idx = -1

if __name__ == '__main__':
    pass
