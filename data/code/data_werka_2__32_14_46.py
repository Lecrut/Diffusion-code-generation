def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

class PhraseMetrics:
    def __init__(self, phrase):
        self.phrase = phrase
    def get_length(self):
        return len(self.phrase)
    def is_empty(self):
        return len(self.phrase) == 0

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        print(calculate_phrase_length(sample_phrase))
        metrics = PhraseMetrics(sample_phrase)
        print(metrics.get_length())
        print(metrics.is_empty())
    except ValueError as e:
        print(e)