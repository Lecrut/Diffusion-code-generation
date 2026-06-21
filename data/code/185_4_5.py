import re

class Tokenizer:
    def __init__(self):
        self.seen = set()

    def tokenize_text(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        return [word for word in words if not (word in self.seen or self.seen.add(word))]

if __name__ == '__main__':
    tokenizer = Tokenizer()
    sample_text1 = "Hello, world! Hello, everyone. Welcome to the world of Python."
    print(tokenizer.tokenize_text(sample_text1))
    sample_text2 = "Python is great. Python is powerful!"
    print(tokenizer.tokenize_text(sample_text2))