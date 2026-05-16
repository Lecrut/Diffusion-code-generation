class StringProcessor:
    def remove_spaces(self, input_string):
        result = ""
        for char in input_string:
            if char != ' ':
                result += char
        return result
if __name__ == '__main__':
    processor = StringProcessor()
    sample1 = "hello world"
    sample2 = "  spaces here  "
    sample3 = "nospaces"
    print(processor.remove_spaces(sample1))
    print(processor.remove_spaces(sample2))
    print(processor.remove_spaces(sample3))