class CharacterAnalyzer:
    def filter_characters(self, input_string):
        alpha_chars = []
        numeric_chars = []
        for char in input_string:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                alpha_chars.append(char)
            elif '0' <= char <= '9':
                numeric_chars.append(char)
        return alpha_chars, numeric_chars
if __name__ == '__main__':
    analyzer = CharacterAnalyzer()
    sample_string = "Hello123World!"
    alpha_list, numeric_list = analyzer.filter_characters(sample_string)
    print("Alphabetic characters:", alpha_list)
    print("Numeric characters:", numeric_list)