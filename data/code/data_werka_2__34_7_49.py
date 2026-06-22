class StringManipulator:
    @staticmethod
    def capitalize_first_letter_of_each_word(input_string):
        words = input_string.split()
        capitalized_words = [StringManipulator.capitalize(word) for word in words]
        return ' '.join(capitalized_words)

    @staticmethod
    def capitalize(word):
        if not word:
            return ''
        return word[0].upper() + word[1:]

if __name__ == '__main__':
    sample_input = "yet another test string with different casing."
    result = StringManipulator.capitalize_first_letter_of_each_word(sample_input)
    print(result)