class CharacterAnalyzer:
    def __init__(self, text):
        self.text = text
    def analyze(self):
        vowels = 0
        consonants = 0
        other_chars = 0
        for char in self.text:
            if 'a' <= char.lower() <= 'z':
                if char.lower() in 'aeiou':
                    vowels += 1
                else:
                    consonants += 1
            else:
                other_chars += 1
        return {
            "total_characters": len(self.text),
            "vowels": vowels,
            "consonants": consonants,
            "other_characters": other_chars
        }
if __name__ == '__main__':
    sample_string = "Hello World 123!"
    analyzer = CharacterAnalyzer(sample_string)
    results = analyzer.analyze()
    print(results)