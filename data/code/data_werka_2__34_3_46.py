class StringCapitalizer:
    def __init__(self, input_string):
        self.input_string = input_string

    def capitalize_first_letter(self):
        return ' '.join(word.capitalize() for word in self.input_string.split())

if __name__ == '__main__':
    sample_string = "this is a test string"
    capitalizer = StringCapitalizer(sample_string)
    capitalized_result = capitalizer.capitalize_first_letter()
    print(capitalized_result)

    another_sample_string = "hello world from python"
    another_capitalizer = StringCapitalizer(another_sample_string)
    another_capitalized_result = another_capitalizer.capitalize_first_letter()
    print(another_capitalized_result)