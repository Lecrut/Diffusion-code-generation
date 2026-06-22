class StringProcessor:
    def remove_spaces(self, strings):
        return [s.replace(" ", "") for s in strings]

if __name__ == '__main__':
    processor = StringProcessor()
    sample_strings = ["Hello World", "This is a test string", "Remove spaces here"]
    result = processor.remove_spaces(sample_strings)
    print(result)