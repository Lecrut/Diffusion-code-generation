class StringListProcessor:
    def __init__(self, string_list):
        if len(string_list) < 2:
            raise ValueError("The list must contain at least two elements.")
        self.string_list = string_list

    def get_second_string(self):
        return self.string_list[1]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    processor = StringListProcessor(sample_strings)
    print(processor.get_second_string())