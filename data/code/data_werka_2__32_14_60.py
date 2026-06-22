class PhraseMetrics:
    MAX_LENGTH = 1000

    @staticmethod
    def validate_phrase(phrase):
        if not isinstance(phrase, str):
            raise ValueError("Input must be a string")
        if len(phrase) > PhraseMetrics.MAX_LENGTH:
            raise ValueError(f"Phrase length exceeds maximum allowed: {PhraseMetrics.MAX_LENGTH}")

    @staticmethod
    def get_length(phrase):
        PhraseMetrics.validate_phrase(phrase)
        return len(phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        print(PhraseMetrics.get_length(sample_phrase))
    except ValueError as e:
        print(e)