class PhraseProcessor:
    def __init__(self, phrase):
        if not isinstance(phrase, str):
            raise ValueError("Input must be a string")
        self.phrase = phrase

    def calculate_length(self):
        return len(self.phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        processor = PhraseProcessor(sample_phrase)
        print(processor.calculate_length())
    except ValueError as e:
        print(e)