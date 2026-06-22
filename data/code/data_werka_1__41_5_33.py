class CaseConverter:
    LOWER = 'lower'
    UPPER = 'upper'
    TITLE = 'title'

    def __init__(self, text):
        self.text = text

    def convert(self, case_type):
        if case_type == self.LOWER:
            return self._to_lower()
        elif case_type == self.UPPER:
            return self._to_upper()
        elif case_type == self.TITLE:
            return self._to_title()
        else:
            raise ValueError("Invalid case type")

    def _to_lower(self):
        return self.text.lower()

    def _to_upper(self):
        return self.text.upper()

    def _to_title(self):
        return self.text.title()

if __name__ == '__main__':
    sample_text = 'HeLlO WoRlD'
    converter = CaseConverter(sample_text)
    
    print(f"Original: {sample_text}")
    print(f"Lowercase: {converter.convert(CaseConverter.LOWER)}")
    print(f"Uppercase: {converter.convert(CaseConverter.UPPER)}")
    print(f"Titlecase: {converter.convert(CaseConverter.TITLE)}")