class StringManipulator:
    DELIMITER = ' '

    @staticmethod
    def capitalize_word(word):
        return word[0].upper() + word[1:] if word else ''

    @classmethod
    def capitalize_first_letter_only(cls, s):
        words = s.split(cls.DELIMITER)
        capitalized_words = [cls.capitalize_word(word) for word in words]
        return cls.DELIMITER.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    result = StringManipulator.capitalize_first_letter_only(sample_input)
    print(result)