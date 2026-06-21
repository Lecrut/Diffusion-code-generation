class StringCaseTransformer:
    def __init__(self, text):
        self.text = text
    
    def transform(self, case_type):
        if case_type == 'lower':
            return self._to_lower()
        elif case_type == 'upper':
            return self._to_upper()
        elif case_type == 'title':
            return self._to_title()
        else:
            raise ValueError("Invalid case type. Use 'lower', 'upper', or 'title'.")
    
    def _to_lower(self):
        return self.text.lower()
    
    def _to_upper(self):
        return self.text.upper()
    
    def _to_title(self):
        return self.text.title()

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    transformer = StringCaseTransformer(sample_input)
    
    lower_case_result = transformer.transform('lower')
    upper_case_result = transformer.transform('upper')
    title_case_result = transformer.transform('title')
    
    print(f"Original: {sample_input}")
    print(f"Lowercase: {lower_case_result}")
    print(f"Uppercase: {upper_case_result}")
    print(f"Titlecase: {title_case_result}")