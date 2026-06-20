class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_first_last(self):
        return self.input_string[0], self.input_string[-1]

if __name__ == '__main__':
    processor = StringProcessor("Hello, World!")
    first_char, last_char = processor.get_first_last()
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")