class StringReverser:

    def reverse(self, text):
        return ''.join(reversed(text))
if __name__ == '__main__':
    test_strings = ['Hello, World!', 'Python 3.9', '', '!_-_a']
    reverser = StringReverser()
    for s in test_strings:
        reversed_s = reverser.reverse(s)
        print(reversed_s)