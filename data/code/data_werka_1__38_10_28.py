class LetterAnalyzer:
    ALPHABET = set('abcdefghijklmnopqrstuvwxyz')

    @staticmethod
    def is_letter(char):
        return char.lower() in LetterAnalyzer.ALPHABET

    def find_repeated_letters(self, input_string):
        seen_letters = set()
        repeated_letters = set()
        for char in input_string:
            if self.is_letter(char):
                lower_char = char.lower()
                if lower_char in seen_letters:
                    repeated_letters.add(lower_char)
                else:
                    seen_letters.add(lower_char)
        return repeated_letters

if __name__ == '__main__':
    analyzer = LetterAnalyzer()
    sample_string = "programming is fun"
    repeated = analyzer.find_repeated_letters(sample_string)
    print("Repeated letters found:", repeated)

    sample_string_2 = "hello world"
    repeated_2 = analyzer.find_repeated_letters(sample_string_2)
    print("Repeated letters in", sample_string_2, ":", repeated_2)