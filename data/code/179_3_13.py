class StringReverser:
    def __init__(self, s):
        self.s = s

    def reverse_words(self):
        return ' '.join(self.s.split()[::-1])

if __name__ == '__main__':
    reverser = StringReverser("The quick brown fox")
    print(reverser.reverse_words())