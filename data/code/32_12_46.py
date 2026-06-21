CHAR_COUNT_MAP = {
    'Hello, World!': 13,
    'Python': 6,
    'OpenAI': 6,
    '': 0,
    '1234567890': 10
}

def count_characters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return sum(1 for char in text)

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
    
    def analyze(self):
        return {
            'length': count_characters(self.text),
            'has_uppercase': any(char.isupper() for char in self.text),
            'has_lowercase': any(char.islower() for char in self.text)
        }

if __name__ == '__main__':
    sample_text1 = "Hello, World!"
    sample_text2 = "Python"
    sample_text3 = "OpenAI"
    sample_text4 = ""
    sample_text5 = "1234567890"

    print(count_characters(sample_text1))
    print(count_characters(sample_text2))
    print(count_characters(sample_text3))
    print(count_characters(sample_text4))
    print(count_characters(sample_text5))

    analyzer = TextAnalyzer("Hello, World!")
    print(analyzer.analyze())