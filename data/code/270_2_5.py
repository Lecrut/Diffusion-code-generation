class StringProcessor:
    @staticmethod
    def clean_string(input_string):
        return input_string.replace(' ', '')
if __name__ == '__main__':
    test_string_1 = "Hello World"
    result_1 = StringProcessor.clean_string(test_string_1)
    print(f"Input: '{test_string_1}', Output: '{result_1}'")
    test_string_2 = "   This has spaces   "
    result_2 = StringProcessor.clean_string(test_string_2)
    print(f"Input: '{test_string_2}', Output: '{result_2}'")
    test_string_3 = "NoSpacesHere"
    result_3 = StringProcessor.clean_string(test_string_3)
    print(f"Input: '{test_string_3}', Output: '{result_3}'")