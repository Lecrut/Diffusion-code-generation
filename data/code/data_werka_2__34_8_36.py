class StringCapitalizer:
    DELIMITER = ' '

    @staticmethod
    def capitalize_word(word):
        return word[0].upper() + word[1:] if word else ''

    def capitalize_first_letter_only(self, s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        words = s.split(self.DELIMITER)
        capitalized_words = [self.capitalize_word(word) for word in words]
        return self.DELIMITER.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    capitalizer = StringCapitalizer()
    result = capitalizer.capitalize_first_letter_only(sample_input)
    print(result)