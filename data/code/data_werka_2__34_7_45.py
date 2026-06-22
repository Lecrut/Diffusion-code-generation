class StringCapitalizer:
    def __init__(self, input_string):
        self.input_string = input_string

    def capitalize_first_letter_of_each_word(self):
        words = self.input_string.split()
        capitalized_words = [word[0].upper() + word[1:] if word else '' for word in words]
        return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input_1 = "hello world! this is a TEST string."
    capitalizer_1 = StringCapitalizer(sample_input_1)
    result_1 = capitalizer_1.capitalize_first_letter_of_each_word()
    print(result_1)

    sample_input_2 = "another example with different casing."
    capitalizer_2 = StringCapitalizer(sample_input_2)
    result_2 = capitalizer_2.capitalize_first_letter_of_each_word()
    print(result_2)