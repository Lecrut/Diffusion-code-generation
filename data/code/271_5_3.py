class CharacterAnalyzer:
    def analyze_string(self, input_string):
        alphabetic_chars = []
        numeric_chars = []
        for char in input_string:
            if char.isalpha():
                alphabetic_chars.append(char)
            elif char.isdigit():
                numeric_chars.append(char)
        return alphabetic_chars, numeric_chars
if __name__ == '__main__':
    analyzer = CharacterAnalyzer()
    sample_string = "abc123def456"
    alphabets, numbers = analyzer.analyze_string(sample_string)
    print(f"Input String: {sample_string}")
    print(f"Alphabetic Characters: {alphabets}")
    print(f"Numeric Characters: {numbers}")