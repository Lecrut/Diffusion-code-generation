class CaseTransformer:
    LOWER = 'lower'
    UPPER = 'upper'
    TITLE = 'title'

    @staticmethod
    def transform(text, case_type):
        if case_type == CaseTransformer.LOWER:
            return text.lower()
        elif case_type == CaseTransformer.UPPER:
            return text.upper()
        elif case_type == CaseTransformer.TITLE:
            return text.title()
        else:
            raise ValueError("Invalid case type")

def case_swap(text):
    return {
        CaseTransformer.LOWER: CaseTransformer.transform(text, CaseTransformer.LOWER),
        CaseTransformer.UPPER: CaseTransformer.transform(text, CaseTransformer.UPPER),
        CaseTransformer.TITLE: CaseTransformer.transform(text, CaseTransformer.TITLE)
    }

if __name__ == '__main__':
    sample_text = "this is a sample sentence"
    result = case_swap(sample_text)
    print(result)