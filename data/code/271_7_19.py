import re

class CharacterCounter:
    UPPERCASE_PATTERN = re.compile('[A-Z]')
    LOWERCASE_PATTERN = re.compile('[a-z]')
    DIGIT_PATTERN = re.compile('\\d')
    PUNCTUATION_PATTERN = re.compile('[^\\w\\s]')

    @staticmethod
    def count_character_types(text):
        if not text:
            return {'uppercase': 0, 'lowercase': 0, 'digits': 0, 'punctuation': 0}
        uppercase_count = len(CharacterCounter.UPPERCASE_PATTERN.findall(text))
        lowercase_count = len(CharacterCounter.LOWERCASE_PATTERN.findall(text))
        digits_count = len(CharacterCounter.DIGIT_PATTERN.findall(text))
        punctuation_count = len(CharacterCounter.PUNCTUATION_PATTERN.findall(text))
        return {'uppercase': uppercase_count, 'lowercase': lowercase_count, 'digits': digits_count, 'punctuation': punctuation_count}
if __name__ == '__main__':
    sample_text = 'Hello, World! 123'
    result = CharacterCounter.count_character_types(sample_text)
    print(result)