class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ' '.join(self.text.split()[::-1])

if __name__ == '__main__':
    reverser = StringReverser("The quick brown fox")
    print(reverser.reverse())