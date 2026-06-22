class StringProcessor:
    @staticmethod
    def remove_spaces(input_string):
        return ''.join(input_string.split())

if __name__ == '__main__':
    processor = StringProcessor()
    test_string1 = "hello world"
    result1 = processor.remove_spaces(test_string1)
    print(result1)
    test_string2 = "   this has spaces   "
    result2 = processor.remove_spaces(test_string2)
    print(result2)
    test_string3 = "no_spaces"
    result3 = processor.remove_spaces(test_string3)
    print(result3)