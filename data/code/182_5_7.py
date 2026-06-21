class CharGenerator:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0

    def get_next_char(self):
        if self.index < len(self.input_string):
            char = self.input_string[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration

if __name__ == '__main__':
    sample_string = 'Hello World'
    generator_instance = CharGenerator(sample_string)
    print(generator_instance.get_next_char())
    print(generator_instance.get_next_char())
    print(generator_instance.get_next_char())