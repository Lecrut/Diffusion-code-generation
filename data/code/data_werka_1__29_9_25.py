class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]

if __name__ == '__main__':
    sample_text = "Hello, World!"
    reverser = StringReverser(sample_text)
    print(reverser.reverse())