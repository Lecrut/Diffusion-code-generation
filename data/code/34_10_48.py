class Capitalizer:
    def __init__(self, text):
        self.text = text

    def capitalize(self):
        words = self.text.split()
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_text = "the quick brown fox jumps over the lazy dog"
    capitalizer = Capitalizer(sample_text)
    result = capitalizer.capitalize()
    print(result)