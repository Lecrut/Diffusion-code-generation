class StringListProcessor:
    def __init__(self, strings):
        if len(strings) < 2:
            raise ValueError("The list must contain at least two elements.")
        self.strings = strings

    def get_second_string(self):
        return self.strings[1]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    processor = StringListProcessor(sample_strings)
    print(processor.get_second_string())