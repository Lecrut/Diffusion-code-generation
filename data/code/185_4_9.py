import re

class Tokenizer:
    def __init__(self):
        self.seen = set()
    
    def tokenize(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        unique_words = []
        for word in words:
            if word not in self.seen:
                unique_words.append(word)
                self.seen.add(word)
        return unique_words

if __name__ == '__main__':
    tokenizer = Tokenizer()
    sample_text = "Hello, world! Hello, everyone. Welcome to the world of Python."
    tokens = tokenizer.tokenize(sample_text)
    print(tokens)