class StringProcessor:
    def remove_spaces(self, input_string):
        return ''.join(input_string.split())

if __name__ == '__main__':
    processor = StringProcessor()
    sample1 = "hello world"
    print(processor.remove_spaces(sample1))
    sample2 = "   this has spaces   "
    print(processor.remove_spaces(sample2))
    sample3 = "no_spaces"
    print(processor.remove_spaces(sample3))