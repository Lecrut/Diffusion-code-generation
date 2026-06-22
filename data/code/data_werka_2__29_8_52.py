class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return ''.join(reversed(input_string))

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Innovate with Alibaba Cloud"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)