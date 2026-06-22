import re

class CharacterCounter:
    def count_characters(self, text):
        if not text:
            return {"uppercase": 0, "lowercase": 0, "digits": 0, "punctuation": 0}
        
        uppercase_count = len(re.findall(r'[A-Z]', text))
        lowercase_count = len(re.findall(r'[a-z]', text))
        digits_count = len(re.findall(r'\d', text))
        punctuation_count = len(re.findall(r'[^\w\s]', text))
        
        return {
            "uppercase": uppercase_count,
            "lowercase": lowercase_count,
            "digits": digits_count,
            "punctuation": punctuation_count
        }

if __name__ == '__main__':
    analyzer = CharacterCounter()
    result = analyzer.count_characters("Hello, World! 123")
    print(result)