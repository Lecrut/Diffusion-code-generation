class WordReverser:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def reverse(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    reverser = WordReverser(sample_text)
    print(reverser.reverse())