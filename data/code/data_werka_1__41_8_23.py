class CaseTransformer:

    def __init__(self, text):
        self.text = text

    def to_lower(self):
        return self.text.lower()

    def to_upper(self):
        return self.text.upper()

    def to_title(self):
        return self.text.title()

def case_swap(text):
    transformer = CaseTransformer(text)
    return {'lower': transformer.to_lower(), 'upper': transformer.to_upper(), 'title': transformer.to_title()}
if __name__ == '__main__':
    sample_text = 'Hello World'
    result = case_swap(sample_text)
    print(result)
    transformer_instance = CaseTransformer('another Example')
    print(transformer_instance.to_lower())
    print(transformer_instance.to_upper())
    print(transformer_instance.to_title())