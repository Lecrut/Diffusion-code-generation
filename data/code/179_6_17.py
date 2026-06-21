class SentenceReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    reverser_instance = SentenceReverser("This is a sample sentence")
    print(reverser_instance.reverse_words())