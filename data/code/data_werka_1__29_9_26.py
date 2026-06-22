class StringReverser:
    def reverse(self, s):
        return s[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Hello, World!"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)