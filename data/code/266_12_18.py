class WordCounter:
    def count_words(self, text):
        if not text.strip():
            return 0
        words = text.split()
        return len(words)

if __name__ == '__main__':
    sample_texts = [
        "This is a sample sentence for testing the word counter.",
        "Another test case with different spacing and punctuation.",
        "",
        "Word one. Word two! Three.",
        "   leading and trailing spaces test   "
    ]
    
    wc = WordCounter()
    for text in sample_texts:
        print(f"Text: '{text}'")
        print(f"Word count: {wc.count_words(text)}")
        print("-" * 20)