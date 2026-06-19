class StringReverser:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reverser = StringReverser(sample_string)
    reversed_string = reverser.reverse()
    print(reversed_string)