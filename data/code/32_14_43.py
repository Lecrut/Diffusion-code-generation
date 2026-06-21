def phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

class PhraseCounter:
    def __init__(self, phrase):
        self.phrase = phrase
    def count_characters(self):
        return len(self.phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        print(phrase_length(sample_phrase))
        counter = PhraseCounter(sample_phrase)
        print(counter.count_characters())
    except ValueError as e:
        print(e)