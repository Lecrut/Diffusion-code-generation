class StringReverser:
    def __init__(self, s):
        self.original = s

    def reverse(self):
        return ''.join(reversed(self.original))

if __name__ == '__main__':
    reverser = StringReverser("hello")
    print(reverser.reverse())
    print(StringReverser("world").reverse())