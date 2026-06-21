class SentenceReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    reverser = SentenceReverser("Hello world from Python")
    print(reverser.reverse())