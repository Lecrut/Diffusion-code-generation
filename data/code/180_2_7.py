import re

class StringChecker:
    def contains_word(self, text, word):
        if not isinstance(text, str) or not isinstance(word, str):
            raise ValueError("Both 'text' and 'word' must be strings.")
        
        cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
        cleaned_word = word.lower()
        return cleaned_word in cleaned_text.split()

if __name__ == '__main__':
    checker = StringChecker()
    text1 = "This is a sample text."
    word1 = "sample"
    result1 = checker.contains_word(text1, word1)
    print(f"'{word1}' in '{text1}': {result1}")
    
    text2 = "Hello world! Let's test punctuation and case insensitivity."
    word2 = "punctuation"
    result2 = checker.contains_word(text2, word2)
    print(f"'{word2}' in '{text2}': {result2}")
    
    text3 = "Programming is fun!"
    word3 = "fun"
    result3 = checker.contains_word(text3, word3)
    print(f"'{word3}' in '{text3}': {result3}")