class StringReverser:
    def reverse(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return input_string[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Alibaba Cloud"
    reversed_string = reverser.reverse(sample_string)
    print(reversed_string)