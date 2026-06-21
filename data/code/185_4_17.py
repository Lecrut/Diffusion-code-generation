import re

class TextTokenizer:
    PUNCTUATION_REGEX = r'[^\w\s]'
    
    @staticmethod
    def remove_punctuation(text):
        return re.sub(TextTokenizer.PUNCTUATION_REGEX, '', text)
    
    @staticmethod
    def tokenize_and_get_unique_words(text):
        cleaned_text = TextTokenizer.remove_punctuation(text).lower()
        words = re.findall(r'\b\w+\b', cleaned_text)
        unique_words = []
        seen = set()
        for word in words:
            if word not in seen:
                unique_words.append(word)
                seen.add(word)
        return unique_words

if __name__ == '__main__':
    sample_text = "Hello, world! Hello, everyone. Welcome to the world of Python."
    tokenizer = TextTokenizer()
    print(tokenizer.tokenize_and_get_unique_words(sample_text))