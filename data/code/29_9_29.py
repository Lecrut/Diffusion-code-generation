class StringReverser:
    def reverse(self, text):
        return text[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Hello, World!"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)