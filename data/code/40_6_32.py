class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def first_letter_of_first_word(self):
        stripped_string = self.input_string.lstrip()
        if not stripped_string:
            return None
        first_space_index = stripped_string.find(' ')
        return stripped_string[0] if first_space_index == -1 else stripped_string[0]

if __name__ == '__main__':
    sample_strings = {
        'example_1': '   Hello world',
        'example_2': '   Example text',
        'example_3': '   Hello World',
        'example_4': '  Hello world',
        'empty_string': '',
        'single_word': 'Single'
    }
    
    for key, value in sample_strings.items():
        processor = StringProcessor(value)
        print(f"{key}: {processor.first_letter_of_first_word()}")