class WordReverser:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

    def get_original_text(self):
        return self.text

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    reverser = WordReverser(sample_text)
    print(reverser.reverse_words())
    print(reverser.get_original_text())