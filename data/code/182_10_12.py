class StringSeparator:
    DELIMITER = ' '

    @staticmethod
    def separate_characters(input_string):
        return StringSeparator.DELIMITER.join(input_string)

if __name__ == '__main__':
    test_string1 = "hello"
    result1 = StringSeparator.separate_characters(test_string1)
    print(result1)
    
    test_string2 = "world"
    result2 = StringSeparator.separate_characters(test_string2)
    print(result2)
    
    test_string3 = ""
    result3 = StringSeparator.separate_characters(test_string3)
    print(result3)