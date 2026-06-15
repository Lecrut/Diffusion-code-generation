class StringProcessor:
    @staticmethod
    def clean_string(input_string: str) -> str:
        return input_string.replace(' ', '')
if __name__ == '__main__':
    sample1 = "Hello World"
    result1 = StringProcessor.clean_string(sample1)
    print(f"Original: '{sample1}'")
    print(f"Cleaned: '{result1}'")
    sample2 = "  This is a test string with spaces  "
    result2 = StringProcessor.clean_string(sample2)
    print(f"Original: '{sample2}'")
    print(f"Cleaned: '{result2}'")
    sample3 = "NoSpacesHere"
    result3 = StringProcessor.clean_string(sample3)
    print(f"Original: '{sample3}'")
    print(f"Cleaned: '{result3}'")