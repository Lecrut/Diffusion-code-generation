class PhraseValidator:
    def __init__(self, phrase):
        self.phrase = phrase

    def validate(self):
        if not isinstance(self.phrase, str):
            raise ValueError("Input must be a string")
        return True

def phrase_length(phrase):
    validator = PhraseValidator(phrase)
    if validator.validate():
        return len(phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        print(phrase_length(sample_phrase))
    except ValueError as e:
        print(e)