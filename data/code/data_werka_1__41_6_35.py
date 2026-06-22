class StringTransformer:
    CASE_TYPE_TITLE = "title"

    def __init__(self, strings):
        self.strings = strings

    def transform_to_title_case(self):
        return [s.title() for s in self.strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON programming", "this is a TEST"]
    transformer = StringTransformer(sample_strings)
    title_cased_strings = transformer.transform_to_title_case()
    print(title_cased_strings)