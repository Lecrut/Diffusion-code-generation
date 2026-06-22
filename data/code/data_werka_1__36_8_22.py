class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ''.join(reversed(self.text))

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    reverser = StringReverser(sample_string)
    reversed_string = reverser.reverse()
    print(reversed_string)