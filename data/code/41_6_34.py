class StringProcessor:
    CASE_TYPE_TITLE = 'title'

    @staticmethod
    def _convert_to_case(input_string, case_type):
        if case_type == StringProcessor.CASE_TYPE_TITLE:
            return input_string.title()
        else:
            raise ValueError("Unsupported case type")

    @staticmethod
    def convert_strings(strings):
        return [StringProcessor._convert_to_case(s, StringProcessor.CASE_TYPE_TITLE) for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON programming", "this is a TEST"]
    title_cased_strings = StringProcessor.convert_strings(sample_strings)
    print(title_cased_strings)