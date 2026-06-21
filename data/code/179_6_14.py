class TextReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_text = ' '.join(words[::-1])
        return reversed_text

if __name__ == '__main__':
    reverser = TextReverser("Hello world from Python")
    print(reverser.reverse_words())