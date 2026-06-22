CHAR_LENGTH_CONSTANT = 1

def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase) * CHAR_LENGTH_CONSTANT

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
    def analyze_length(self):
        return len(self.text) * CHAR_LENGTH_CONSTANT

if __name__ == '__main__':
    sample_text = "Hello, World!"
    try:
        print(calculate_phrase_length(sample_text))
        analyzer = TextAnalyzer(sample_text)
        print(analyzer.analyze_length())
    except ValueError as e:
        print(e)