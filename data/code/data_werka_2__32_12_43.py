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
            'is_empty': len(self.text) == 0,
            'has_numbers': any(char.isdigit() for char in self.text)
        }

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Python",
        "OpenAI",
        "",
        "1234567890"
    ]
    
    for text in sample_texts:
        analyzer = TextAnalyzer(text)
        result = analyzer.analyze()
        print(f"Text: '{text}' - Length: {result['length']}, Is Empty: {result['is_empty']}, Has Numbers: {result['has_numbers']}")