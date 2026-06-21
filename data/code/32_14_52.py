class PhraseUtility:
    DEFAULT_PHRASE = "Hello, World!"
    
    @staticmethod
    def calculate_length(phrase):
        return len(phrase)
    
    @classmethod
    def get_phrase_length(cls, phrase=DEFAULT_PHRASE):
        if not isinstance(phrase, str):
            raise ValueError("Input must be a string")
        return cls.calculate_length(phrase)

if __name__ == '__main__':
    sample_phrase = "Alibaba Cloud"
    print(PhraseUtility.get_phrase_length(sample_phrase))
    print(PhraseUtility.get_phrase_length())