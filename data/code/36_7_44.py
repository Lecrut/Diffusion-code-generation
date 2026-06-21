class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]

    def get_input(self):
        return self.input_string

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    reverser = StringReverser(sample_string)
    print(reverser.reverse())
    print(reverser.get_input())