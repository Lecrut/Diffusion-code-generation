class StringReverser:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def reverse(self):
        return self.input_string[::-1]

if __name__ == '__main__':
    try:
        sample_input = "Hello, World!"
        reverser = StringReverser(sample_input)
        print(reverser.reverse())
    except ValueError as e:
        print(e)