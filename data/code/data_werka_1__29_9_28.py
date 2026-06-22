class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reverser = StringReverser(sample_string)
    reversed_string = reverser.reverse()
    print(reversed_string)