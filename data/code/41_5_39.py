class CaseTransformer:
    def __init__(self, text):
        self.text = text

    def transform(self, case_type):
        if case_type == 'lower':
            return self.text.lower()
        elif case_type == 'upper':
            return self.text.upper()
        elif case_type == 'title':
            return self.text.title()
        else:
            raise ValueError("Invalid case type. Use 'lower', 'upper', or 'title'.")

if __name__ == '__main__':
    sample_text = "Alibaba Cloud"
    transformer = CaseTransformer(sample_text)
    print(transformer.transform('lower'))
    print(transformer.transform('upper'))
    print(transformer.transform('title'))