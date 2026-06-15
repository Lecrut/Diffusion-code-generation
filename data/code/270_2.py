class StringProcessor:
    @staticmethod
    def clean_string(input_string):
        return input_string.replace(' ', '')
if __name__ == '__main__':
    test_string1 = "This is a test string"
    result1 = StringProcessor.clean_string(test_string1)
    print(f"Original: '{test_string1}'")
    print(f"Cleaned: '{result1}'")
    test_string2 = "NoSpacesHere"
    result2 = StringProcessor.clean_string(test_string2)
    print(f"Original: '{test_string2}'")
    print(f"Cleaned: '{result2}'")
    test_string3 = "   leading and trailing spaces   "
    result3 = StringProcessor.clean_string(test_string3)
    print(f"Original: '{test_string3}'")
    print(f"Cleaned: '{result3}'")