class CaseTransformer:
    CASE_LOWER = 'lower'
    CASE_UPPER = 'upper'
    CASE_TITLE = 'title'

    @staticmethod
    def transform(text):
        return {
            CaseTransformer.CASE_LOWER: text.lower(),
            CaseTransformer.CASE_UPPER: text.upper(),
            CaseTransformer.CASE_TITLE: text.title()
        }

if __name__ == '__main__':
    sample_text = "this is a sample sentence"
    result = CaseTransformer.transform(sample_text)
    print(result)