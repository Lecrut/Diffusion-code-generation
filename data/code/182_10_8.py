class StringSeparator:
    DELIMITER = ", "

    @staticmethod
    def separate_characters(input_string):
        return StringSeparator.DELIMITER.join(input_string)

if __name__ == '__main__':
    test_string = "Hello World"
    result = StringSeparator.separate_characters(test_string)
    print(result)