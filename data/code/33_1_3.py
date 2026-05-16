class StringProcessor:
    def remove_spaces(self, input_string):
        result = ""
        for char in input_string:
            if char != ' ':
                result += char
        return result
if __name__ == '__main__':
    processor = StringProcessor()
    test_string1 = "hello world"
    test_string2 = "  this has spaces  "
    test_string3 = "nospaces"
    test_string4 = "   "
    print(processor.remove_spaces(test_string1))
    print(processor.remove_spaces(test_string2))
    print(processor.remove_spaces(test_string3))
    print(processor.remove_spaces(test_string4))