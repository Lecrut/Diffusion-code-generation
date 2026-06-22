def validate_input(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")

def phrase_length(phrase):
    validate_input(phrase)
    return len(phrase)

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        validate_input(self.text)
    
    def get_length(self):
        return len(self.text)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        print(phrase_length(sample_phrase))
        analyzer = TextAnalyzer(sample_phrase)
        print(analyzer.get_length())
    except ValueError as e:
        print(e)