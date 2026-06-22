class StringManipulator:
    SEPARATOR = ' '

    @staticmethod
    def capitalize_first_letter(s):
        words = s.split(StringManipulator.SEPARATOR)
        capitalized_words = [word.capitalize() for word in words]
        return StringManipulator.SEPARATOR.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "this is another test string"
    result = StringManipulator.capitalize_first_letter(sample_string)
    print(result)