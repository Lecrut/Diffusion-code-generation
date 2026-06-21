def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return word[::-1]

class WordProcessor:
    def __init__(self, text):
        self.text = text

    def get_reversed_text(self):
        return reverse_word(self.text)

if __name__ == '__main__':
    sample_text = "challenge"
    processor = WordProcessor(sample_text)
    reversed_text = processor.get_reversed_text()
    print(reversed_text)