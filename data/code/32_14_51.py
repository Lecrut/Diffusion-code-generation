def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

class StringAnalyzer:
    def __init__(self, text):
        self.text = text
    def analyze_length(self):
        return len(self.text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    try:
        print(calculate_phrase_length(sample_text))
        analyzer = StringAnalyzer(sample_text)
        print(analyzer.analyze_length())
    except ValueError as e:
        print(e)