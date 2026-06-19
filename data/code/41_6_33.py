class TitleCaseConverter:
    @staticmethod
    def convert_list_to_title_case(strings):
        return [TitleCaseConverter._convert_single_to_title_case(s) for s in strings]

    @staticmethod
    def _convert_single_to_title_case(string):
        return string.title()

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON programming", "this is a TEST"]
    title_cased_strings = TitleCaseConverter.convert_list_to_title_case(sample_strings)
    print(title_cased_strings)