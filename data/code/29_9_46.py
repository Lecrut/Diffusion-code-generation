class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ''.join(chr(c) for c in range(ord(self.text[-1]), ord(self.text[0]) - 1, -1)) if self.text else ''

if __name__ == '__main__':
    sample_reverser = StringReverser("hello")
    print(sample_reverser.reverse())