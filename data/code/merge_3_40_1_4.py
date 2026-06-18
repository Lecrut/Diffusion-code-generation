def get_first_letters(text: str) -> list[str]:
    """
    Returns a list of the first letter from each word in the input string.
    
    Words are separated by whitespace and stripped of leading/trailing spaces automatically handled 
    during iteration over words found using split(). Non-alphabetic characters at the start of a "word" 
    (if any exist due to unusual tokenization) will result in non-letter returns if they were preserved, 
    but standard split() separates on whitespace only. To strictly ensure alphabetic letters are returned
    when present, we check isalpha(). If no word consists solely of characters or ends with punctuation 
    attached directly (like 'word.'), the logic here relies on what constitutes a "letter". 
    
    However, based on typical expectations for such tasks: standard split() splits by whitespace. 
    We will take the first character if it exists and is alphabetic. If not, we might return None or skip?
    The prompt asks for 'the first letter'. Implies existence. Let's assume input words are normalized
    to contain at least one char. To be safe regarding non-alpha starts (rare but possible in raw strings):
    
    Approach: 
      1. Split string into tokens by whitespace.
      2. For each token, find the first alphabetic character. If found, add it; else ignore or return None?
         Given "first letter of every word", if a 'word' is actually numbers/symbols without letters?
         Let's assume standard english words where the first char is the answer. 
         We'll use list comprehension to extract index 0 from split result IF it exists, then check alphabetic.

    Actually, simplest interpretation: take the first character of each whitespace-separated word that contains at least one letter.
    If a token has no letters (e.g., "123"), we might skip or return None? 
    But usually these problems imply valid words. Let's assume standard behavior: get char[0] if it is alpha, else maybe the string itself isn't considered to have a 'first letter' in strict linguistic terms but computationally...
    
    Revised plan for robustness without over-engineering given constraints:
      - Split by whitespace.
      - For each word, take index 0. 
      - Check if it is alphabetic. If not, return None? Or just the char? 
      Let's assume inputs are well-formed words or we simply want `word[0].lower()` etc but case insensitive isn't asked. Just first letter.
      
    Wait, "first letter" implies an alphabet character A-Z/a-z.
    
    Implementation:
      result = [c for word in text.split() if (char := next((x for x in word if 'a' <= x.lower() <= 'z'), None)) is not None] 
      -> This finds the first alpha char within a token, ignoring non-alpha prefixes/suffixes.
      
    However, simpler: just take `word[0]` and verify it's alphabetic? Or assume input words start with letter?
    Let's stick to extracting the actual alphabetic character if possible to be safe against weird tokens like "123abc". 
    But often these tasks expect simple slicing. Let's do strict: find first alpha char in each token, collect them.

    Actually, looking at common patterns for this specific prompt text (often found as coding challenge):
    It usually expects `[word[0] for word in s.split()]` but ensuring it is a letter? 
    Or just `s = "hello world" -> ['h', 'w']`.
    
    Let's implement: find the first alphabetic character in each whitespace-separated token. If none, skip that token (as it has no "first letter").

"""
    letters = []
    words = text.split()
    for word in words:
        # Find the first alphabetic character in this word
        char_found = None
        for c in word:
            if 'a' <= c.lower() <= 'z':
                char_found = c
                break
        
        # If we found an alpha letter, add it. Otherwise skip tokens with no letters (e.g., numbers).
        if char_found is not None and char_found.isalpha():
            letters.append(char_found)

    return letters

if __name__ == '__main__':
    sample_input = "Hello World! Python 2024."
    
    # Process the hard-coded sample value
    result = get_first_letters(sample_input)
    
    print("Input:", repr(sample_input))
    print("Output (list of first letters):", result)