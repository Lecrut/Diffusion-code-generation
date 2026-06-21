def phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def get_length(self):
        return len(self.text)

    def is_empty(self):
        return self.get_length() == 0

if __name__ == '__main__':
    SAMPLE_PHRASE = "Hello, World!"
    try:
        print(phrase_length(SAMPLE_PHRASE))
        analyzer = TextAnalyzer(SAMPLE_PHRASE)
        print(analyzer.get_length())
        print(analyzer.is_empty())
    except ValueError as e:
        print(e)