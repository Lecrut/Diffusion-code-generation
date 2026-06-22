def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

class PhraseProcessor:
    def __init__(self, phrase):
        self.phrase = phrase

    def get_length(self):
        return calculate_phrase_length(self.phrase)

if __name__ == '__main__':
    sample_phrases = ["Hello, World!", "Optimized function", "", "Python programming"]
    for phrase in sample_phrases:
        processor = PhraseProcessor(phrase)
        print(processor.get_length())