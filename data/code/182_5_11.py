class CharacterGenerator:
    @staticmethod
    def generate_characters(input_string):
        for char in input_string:
            yield char

if __name__ == '__main__':
    sample_string = "Hello World"
    generator = CharacterGenerator.generate_characters(sample_string)
    result_list = list(generator)
    print(result_list)