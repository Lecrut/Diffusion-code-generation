class StringTransformer:
    @staticmethod
    def to_title_case(strings):
        return [StringTransformer._title_case(s) for s in strings]

    @staticmethod
    def _title_case(string):
        return string.title()

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON programming", "this is a TEST"]
    title_cased_strings = StringTransformer.to_title_case(sample_strings)
    print(title_cased_strings)