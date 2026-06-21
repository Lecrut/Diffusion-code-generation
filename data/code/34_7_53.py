class StringManipulator:
    @staticmethod
    def capitalize_first_letter_of_each_word(input_string):
        return ' '.join(word[0].upper() + word[1:] if word else '' for word in input_string.split())

if __name__ == '__main__':
    sample_input = "yet another example with different casing."
    result = StringManipulator.capitalize_first_letter_of_each_word(sample_input)
    print(result)