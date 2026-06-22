class StringProcessor:
    def remove_spaces(self, strings):
        return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    processor = StringProcessor()
    sample_strings = ["Hello World", "Python Programming", "Remove Spaces"]
    result = processor.remove_spaces(sample_strings)
    print(result)