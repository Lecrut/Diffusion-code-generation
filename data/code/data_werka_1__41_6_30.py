class StringProcessor:
    @staticmethod
    def is_valid_string_list(strings):
        return isinstance(strings, list) and all(isinstance(s, str) for s in strings)

    @staticmethod
    def convert_to_title_case(strings):
        if not StringProcessor.is_valid_string_list(strings):
            raise ValueError("Input must be a list of strings")
        
        return [s.title() for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON programming", "this is a TEST"]
    try:
        title_cased_strings = StringProcessor.convert_to_title_case(sample_strings)
        print(title_cased_strings)
    except ValueError as e:
        print(e)