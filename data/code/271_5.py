class CharacterAnalyzer:
    def filter_characters(self, input_string):
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
    sample_string = "a1b2c3d4e5f"
    alphabets, numbers = analyzer.filter_characters(sample_string)
    print(f"Input String: {sample_string}")
    print(f"Alphabetic Characters: {alphabets}")
    print(f"Numeric Characters: {numbers}")