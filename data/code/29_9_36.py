class StringReverser:
    def reverse(self, input_string):
        reversed_chars = []
        for char in input_string:
            reversed_chars.insert(0, char)
        return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    reverser = StringReverser()
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)