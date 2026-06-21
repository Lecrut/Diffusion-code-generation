class StringProcessor:
    @staticmethod
    def remove_extra_spaces(text: str) -> str:
        return ' '.join(word for word in text.split())

    @classmethod
    def tokenize_string(cls, text: str) -> list[str]:
        cleaned_text = cls.remove_extra_spaces(text)
        return [word for word in cleaned_text.strip().split() if word]

if __name__ == '__main__':
    sample_sentence = "  Hello world! This is a test sentence with multiple spaces. "
    tokens = StringProcessor.tokenize_string(sample_sentence)
    print(tokens)