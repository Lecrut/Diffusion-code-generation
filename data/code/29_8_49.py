class StringReverser:
    def reverse(self, s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return s[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Hello, World!"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)