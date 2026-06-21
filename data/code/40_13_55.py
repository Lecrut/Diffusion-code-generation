import re

class TextAnalyzer:
    ALPHABET_PATTERN = re.compile(r'[a-zA-Z]')

    @staticmethod
    def find_first_letter(text):
        match = TextAnalyzer.ALPHABET_PATTERN.search(text)
        return match.group(0) if match else None

if __name__ == '__main__':
    sample_values = [
        "987xyz",
        "~!@#$%",
        "OpenAI is awesome!",
        "",
        "123456"
    ]
    for value in sample_values:
        result = TextAnalyzer.find_first_letter(value)
        print(result)