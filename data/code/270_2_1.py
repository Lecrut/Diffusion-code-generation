class StringProcessor:
    @staticmethod
    def clean_string(input_string):
        return input_string.replace(' ', '')
if __name__ == '__main__':
    test_string_1 = "This is a test string"
    result_1 = StringProcessor.clean_string(test_string_1)
    print(f"Original: {test_string_1}")
    print(f"Cleaned: {result_1}")
    test_string_2 = "NoSpacesHere"
    result_2 = StringProcessor.clean_string(test_string_2)
    print(f"Original: {test_string_2}")
    print(f"Cleaned: {result_2}")
    test_string_3 = "   leading and trailing spaces   "
    result_3 = StringProcessor.clean_string(test_string_3)
    print(f"Original: '{test_string_3}'")
    print(f"Cleaned: '{result_3}'")