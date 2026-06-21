class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def capitalize_first_letter_of_each_word(self):
        return ' '.join(word[0].upper() + word[1:] if word else '' for word in self.input_string.split())

if __name__ == '__main__':
    sample_input = "hello world! this is a TEST string."
    manipulator = StringManipulator(sample_input)
    result = manipulator.capitalize_first_letter_of_each_word()
    print(result)