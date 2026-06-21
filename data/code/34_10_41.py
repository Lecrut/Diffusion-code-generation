class TitleCaseTransformer:
    def __init__(self, text):
        self.text = text

    def transform(self):
        return ' '.join(word.capitalize() for word in self.text.split())

if __name__ == '__main__':
    sample_text1 = "hello from alibaba cloud"
    transformer1 = TitleCaseTransformer(sample_text1)
    print(transformer1.transform())

    sample_text2 = "welcome to the future of ai"
    transformer2 = TitleCaseTransformer(sample_text2)
    print(transformer2.transform())