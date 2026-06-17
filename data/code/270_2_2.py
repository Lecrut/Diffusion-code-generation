class StringProcessor:
    @staticmethod
    def clean_string(input_string):
        return input_string.replace(' ', '')
if __name__ == '__main__':
    test_string1 = "Hello World"
    result1 = StringProcessor.clean_string(test_string1)
    print(f"Original: '{test_string1}', Cleaned: '{result1}'")
    test_string2 = "   This has many spaces   "
    result2 = StringProcessor.clean_string(test_string2)
    print(f"Original: '{test_string2}', Cleaned: '{result2}'")
    test_string3 = "NoSpacesHere"
    result3 = StringProcessor.clean_string(test_string3)
    print(f"Original: '{test_string3}', Cleaned: '{result3}'")