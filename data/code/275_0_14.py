class StringProcessor:
    @staticmethod
    def uppercase_strings(string_list):
        return [s.upper() for s in string_list]

if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "script"]
    processor = StringProcessor()
    uppercased_strings = processor.uppercase_strings(sample_list)
    for upper_string in uppercased_strings:
        print(upper_string)