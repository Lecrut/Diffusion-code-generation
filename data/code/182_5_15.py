class CharacterGenerator:
    def __init__(self, input_string):
        self.input_string = input_string

    @staticmethod
    def create_generator(input_string):
        return (char for char in input_string)

if __name__ == '__main__':
    sample_string = "Hello World"
    generator = CharacterGenerator.create_generator(sample_string)
    result_list = list(generator)
    print(result_list)