class CaseTransformer:
    LOWER_KEY = 'lower'
    UPPER_KEY = 'upper'
    TITLE_KEY = 'title'

    @staticmethod
    def transform(text):
        return {
            CaseTransformer.LOWER_KEY: text.lower(),
            CaseTransformer.UPPER_KEY: text.upper(),
            CaseTransformer.TITLE_KEY: text.title()
        }

if __name__ == '__main__':
    sample_text = "Hello World"
    result = CaseTransformer.transform(sample_text)
    print(result)