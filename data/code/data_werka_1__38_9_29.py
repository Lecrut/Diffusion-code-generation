class StringAnalyzer:
    @staticmethod
    def find_repeated_letters(input_string):
        repeated_letters = []
        seen_letters = set()
        for letter in input_string:
            if letter.isalpha() and letter.lower() in seen_letters:
                if letter.lower() not in repeated_letters:
                    repeated_letters.append(letter.lower())
            else:
                seen_letters.add(letter.lower())
        return repeated_letters

if __name__ == '__main__':
    sample_input = "This is a simple test string with some repeated letters."
    analyzer = StringAnalyzer()
    result = analyzer.find_repeated_letters(sample_input)
    print(result)