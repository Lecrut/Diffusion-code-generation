class StringProcessor:
    def clean_string(self, input_string: str) -> str:
        return input_string.replace(' ', '')
if __name__ == '__main__':
    processor = StringProcessor()
    sample1 = "Hello World"
    sample2 = "  This is a test string  "
    sample3 = "NoSpacesHere"
    sample4 = "   "
    result1 = processor.clean_string(sample1)
    result2 = processor.clean_string(sample2)
    result3 = processor.clean_string(sample3)
    result4 = processor.clean_string(sample4)
    print(f"Original: '{sample1}', Cleaned: '{result1}'")
    print(f"Original: '{sample2}', Cleaned: '{result2}'")
    print(f"Original: '{sample3}', Cleaned: '{result3}'")
    print(f"Original: '{sample4}', Cleaned: '{result4}'")