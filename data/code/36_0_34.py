class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    reverser = StringReverser(sample_input)
    reversed_output = reverser.reverse()
    print(reversed_output)