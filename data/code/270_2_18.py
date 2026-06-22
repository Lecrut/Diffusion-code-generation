class StringProcessor:
    def remove_spaces(self, s):
        return ''.join(c for c in s if c != ' ')

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello, World! This is a test."
    result = processor.remove_spaces(sample_string)
    print(result)