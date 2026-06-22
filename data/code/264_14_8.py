import re

class WordTokenizer:
    def tokenize_and_filter(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        return sorted(list(set(words)))

if __name__ == '__main__':
    tokenizer = WordTokenizer()
    sample_text = "Hello World! This is a Test string with numbers 123 and symbols @#$"
    result = tokenizer.tokenize_and_filter(sample_text)
    print(result)