class StringListProcessor:
    def __init__(self, strings):
        self.strings = strings

    def get_second_string(self):
        if len(self.strings) < 2:
            raise ValueError("The list must contain at least two elements.")
        return self.strings[1]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    processor = StringListProcessor(sample_strings)
    try:
        second_string = processor.get_second_string()
        print(second_string)
    except ValueError as e:
        print(e)