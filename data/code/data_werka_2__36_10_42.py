class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse(self):
        return ''.join(reversed(self.input_string))

if __name__ == '__main__':
    reverser = StringReverser("hello")
    print(reverser.reverse())