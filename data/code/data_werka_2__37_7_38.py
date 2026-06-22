class StringProcessor:
    def __init__(self):
        self.strings = []

    def add_string(self, s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string.")
        self.strings.append(s)

    def combine_strings(self):
        if len(self.strings) != 2:
            raise ValueError("Exactly two strings are required to combine.")
        return f"{self.strings[0]} {self.strings[1]}"

if __name__ == '__main__':
    processor = StringProcessor()
    try:
        processor.add_string("Hello")
        processor.add_string("World")
        combined_result = processor.combine_strings()
        print(combined_result)
    except ValueError as e:
        print(e)