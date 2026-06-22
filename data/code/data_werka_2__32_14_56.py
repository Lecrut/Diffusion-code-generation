class PhraseUtility:
    MAX_LENGTH = 1000

    @staticmethod
    def validate_phrase(phrase):
        if not isinstance(phrase, str):
            raise ValueError("Input must be a string")
        if len(phrase) > PhraseUtility.MAX_LENGTH:
            raise ValueError(f"Phrase length exceeds maximum allowed ({PhraseUtility.MAX_LENGTH})")

    @staticmethod
    def calculate_length(phrase):
        return len(phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        PhraseUtility.validate_phrase(sample_phrase)
        length = PhraseUtility.calculate_length(sample_phrase)
        print(length)
    except ValueError as e:
        print(e)