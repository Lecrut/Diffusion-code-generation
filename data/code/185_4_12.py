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
    sample_text1 = "Hello, world! Hello, everyone. Welcome to the world of Python."
    print(tokenizer.tokenize(sample_text1))
    
    sample_text2 = "Python is great. Python is powerful. Python is everywhere!"
    print(tokenizer.tokenize(sample_text2))