class StringReverser:
    def reverse(self, input_string):
        return self._reverse_string(input_string)

    def _reverse_string(self, s):
        reversed_chars = []
        for char in s:
            reversed_chars.insert(0, char)
        return ''.join(reversed_chars)

if __name__ == '__main__':
    SAMPLE_STRING = "Hello, World!"
    reverser = StringReverser()
    reversed_string = reverser.reverse(SAMPLE_STRING)
    print(reversed_string)