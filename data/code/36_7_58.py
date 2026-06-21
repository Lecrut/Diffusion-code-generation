class UnicodeReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ''.join(reversed(self.text))

    def get_original_text(self):
        return self.text

if __name__ == '__main__':
    sample_text = "Hello, 世界!"
    reverser = UnicodeReverser(sample_text)
    print(reverser.reverse())
    print(reverser.get_original_text())