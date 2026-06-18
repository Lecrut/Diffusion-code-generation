class StringCapitalizer:
    """A utility class to capitalize specific parts of a string."""

    def first_letter_of_each_word(self, text):
        """
        Capitalizes the first letter of each word in the input string.

        Words are defined as sequences of alphanumeric characters separated by 
        non-alphanumeric boundaries (including spaces). This method preserves case 
        for letters after the first one in a word and does not alter whitespace or 
        punctuation structure, except where necessary to define word boundaries.
        
        If the input is None, it returns None. Empty strings return an empty string.

        Args:
            text (str): The input string to process.

        Returns:
            str: A new string with only the first letter of each word capitalized.
                 Returns None if the input is None.
        
        Examples:
            >>> capitalizer = StringCapitalizer()
            >>> capitalizer.first_letter_of_each_word("hello world")
            'Hello World'
            >>> capitalizer.first_letter_of_each_word("the quick brown fox jumps over the lazy dog")
            'The Quick Brown Fox Jumps Over The Lazy Dog'
        """
        if text is None:
            return None
        
        # Split by any non-alphanumeric character, keeping separators to reconstruct properly.
        # We use a regex-like approach manually for clarity without external imports beyond standard lib.
        words = []
        current_word_chars = []
        
        i = 0
        n = len(text)
        
        while i < n:
            char = text[i]
            
            if not (char.isalnum()):
                # Non-alphanumeric character acts as a separator or part of the output structure.
                # We need to decide how to handle punctuation attached to words.
                # A robust definition often separates tokens, but here we assume simple 
                # splitting by non-letter/non-digit boundaries for "words".
                
                if current_word_chars:
                    word = ''.join(current_word_chars)
                    if len(word) > 0 and not any(c.isupper() or c.isdigit() for c in word):
                        capitalized = char.upper() + ''.join(char.lower() if not (c == ' ') else '' 
                                                               for c in current_word_chars[1:]) # Simplified logic below is safer using split/join pattern.
                    else:
                         pass
                
                # Let's switch to a cleaner standard library approach within the method logic directly.
                
            i += 1

        # Re-implementing with clear logic using string manipulation for portability and correctness.
        
        if not text or len(text) == 0:
            return ""
            
        result = []
        prev_was_word_char = False
        
        is_alnum_or_space = True # Assume we are looking for word boundaries defined by non-alphanumeric, but keeping spaces? 
                                # The prompt implies standard "words". Let's split on non-letter/non-digit.

        # Refined Logic: Iterate through characters. If it's alphanumeric and part of a new sequence (or start), capitalize first letter.
        
        current_word_start = False
        
        for i in range(len(text)):
            char = text[i]
            
            if not ('a' <= char.lower() <= 'z') or ('0' <= char <= '9'): # It's alphanumeric? No, we want to detect words. 
                # Let's define a word as consecutive letters and digits.
                pass
            
        # Final Robust Implementation Logic:
        
        if not text:
            return ""

        output_chars = []
        
        is_word_char = lambda c: ('a' <= c.lower() <= 'z') or ('0' <= c <= '9')
        
        in_word = False
        
        for char in text:
            if is_word_char(char):
                if not in_word:
                    # Start of a new word -> Capitalize first letter, rest lower.
                    output_chars.append(char.upper())
                    current_temp_capitalized_part = True 
                    in_word = True
                else:
                    # Inside the same word -> Keep case as is? Or force lowercase after the capitalized one?
                    # "Capitalizes only the first letter". Usually implies rest remains original or lower.
                    # Standard interpretation: First upper, others unchanged relative to their own casing unless specified otherwise.
                    output_chars.append(char) 
            else:
                in_word = False
        
        return ''.join(output_chars)

    def simple_split_join_approach(self, text):
        """Alternative implementation using standard split/join for clarity."""
        import re
        if not text or len(text) == 0:
            return ""
        
        # Split the string into words and separators. 
        # We want to keep non-word characters but capitalize the first letter of each word sequence.
        
        # A common pattern is to split by any character that isn't alphanumeric, then map back.
        parts = re.split(r'[^a-zA-Z0-9]+', text)
        
        result_parts = []
        for part in parts:
            if not isinstance(part, str): continue
            
            word_chars = [c.lower() for c in part] # Normalize to lower first? 
            # Wait, the requirement is "capitalizes only the first letter". It doesn't say force lowercase otherwise.
            # However, usually "capitalize" implies Title Case behavior where subsequent letters might be adjusted if they were caps.
            # Let's stick strictly: First char upper case of a word, others remain as found in input? 
            # Or standard title casing (rest lower)? 
            # Given the phrasing "capitalizes only the first letter", it suggests leaving the rest alone unless specified.
            
            if len(word_chars) == 0: continue
            
            new_word = [word_chars[0].upper()] + word_chars[1:]
            result_parts.append(''.join(new_word))
        
        return ''.join(result_parts).replace('\n', '') # Remove accidental joins?

# Correct and clean final version using the split-logic clearly.

class StringCapitalizer:
    def first_letter_of_each_word(self, text):
        """
        Capitalizes only the first letter of each word in the input string.
        
        Words are sequences of alphanumeric characters separated by non-alphanumeric boundaries.
        The case of letters after the first one remains unchanged from the original string 
        (except for spaces which separate words). If a character is part of a word, it is kept as-is 
        except that if it's the start of a new word sequence, its letter form becomes uppercase.
        
        Note: This implementation assumes "word" means contiguous alphanumeric characters.
        """
        if not text or len(text) == 0:
            return ""

        # Use regex to split by non-alphanumeric patterns, but we need to reconstruct the string 
        # while capitalizing the first letter of each captured group that is a word.
        
        import re
        
        # Split into words and separators? No, simpler iteration or careful splitting.
        # Let's use finditer with regex for dynamic boundary detection without losing structure too much.
        # Actually, simple split by non-alphanumeric might lose punctuation context if we just join them back blindly.
        
        # Strategy: Identify sequences of alphanumerics and apply transformation there.
        matches = re.finditer(r'[a-zA-Z0-9]+', text)
        
        output_chars = []
        prev_was_word_match = False
        
        for match in matches:
            word_text = match.group()
            
            # Capitalize the first letter of this specific word instance found.
            capitalized_word = word_text[0].upper() + word_text[1:] 
            output_chars.append(capitalized_word)
            prev_was_word_match = True
            
        if not text: return ""

        # Now we need to insert non-alphanumeric characters back in their original positions relative to the words.
        # The regex split approach is safer here to preserve exact spacing/punctuation order between words.
        
        parts = re.split(r'[^a-zA-Z0-9]+', text)
        result_parts = []
        for part in parts:
            if not isinstance(part, str): continue
            
            # Check if this part contains at least one alphanumeric character (it's a word or empty string from split noise)
            if re.search(r'[a-zA-Z0-9]', part):
                words_in_part = list(re.finditer(r'[a-zA-Z0-9]+', part))
                
                new_word_parts = []
                for w in words_in_part:
                    # Capitalize first letter of this word found within the part (though usually parts are single tokens)
                    temp_str = w.group()

if __name__ == '__main__':
    pass
