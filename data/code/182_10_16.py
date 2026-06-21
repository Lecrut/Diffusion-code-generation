class CharacterSeparator:
    DELIMITER = ", "

    @staticmethod
    def separate_characters(input_string):
        return CharacterSeparator.DELIMITER.join(input_string)

if __name__ == '__main__':
    test_string1 = "hello"
    result1 = CharacterSeparator.separate_characters(test_string1)
    print(result1)

    test_string2 = "world"
    result2 = CharacterSeparator.separate_characters(test_string2)
    print(result2)

    test_string3 = ""
    result3 = CharacterSeparator.separate_characters(test_string3)
    print(result3)

    test_string4 = "Python"
    result4 = CharacterSeparator.separate_characters(test_string4)
    print(result4)