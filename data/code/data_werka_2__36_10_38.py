class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ''.join(reversed(self.text))

if __name__ == '__main__':
    reverser = StringReverser("hello")
    print(reverser.reverse())
    print(StringReverser("world").reverse())