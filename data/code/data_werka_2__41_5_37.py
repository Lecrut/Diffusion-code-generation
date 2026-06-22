class StringCaseTransformer:
    CASE_LOWER = 'lower'
    CASE_UPPER = 'upper'
    CASE_TITLE = 'title'

    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def transform(self, case_type):
        if case_type == self.CASE_LOWER:
            return self._to_lower()
        elif case_type == self.CASE_UPPER:
            return self._to_upper()
        elif case_type == self.CASE_TITLE:
            return self._to_title()
        else:
            raise ValueError(f"Unsupported case type: {case_type}")

    def _to_lower(self):
        return self.text.lower()

    def _to_upper(self):
        return self.text.upper()

    def _to_title(self):
        return self.text.title()

if __name__ == '__main__':
    sample_string = "Example String"
    transformer = StringCaseTransformer(sample_string)
    
    print("Original:", sample_string)
    print("Lowercase:", transformer.transform(StringCaseTransformer.CASE_LOWER))
    print("Uppercase:", transformer.transform(StringCaseTransformer.CASE_UPPER))
    print("Titlecase:", transformer.transform(StringCaseTransformer.CASE_TITLE))