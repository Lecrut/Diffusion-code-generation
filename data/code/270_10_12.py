class StringProcessor:
    def __init__(self, strings):
        self.strings = strings

    def remove_spaces(self):
        return [s.replace(' ', '') for s in self.strings]

if __name__ == '__main__':
    sample_strings = ["Hello World", "Python Programming", "Remove Spaces"]
    processor = StringProcessor(sample_strings)
    result = processor.remove_spaces()
    print(result)