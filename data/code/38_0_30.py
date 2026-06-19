class LetterChecker:
    ALPHABET = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @staticmethod
    def is_letter(char):
        return char in LetterChecker.ALPHABET

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
        return sorted(list(repeated_letters))

if __name__ == '__main__':
    checker = LetterChecker()
    sample_string_1 = "programming"
    sample_string_2 = "hello world"
    print("Repeated letters in", sample_string_1, ":", checker.find_repeated_letters(sample_string_1))
    print("Repeated letters in", sample_string_2, ":", checker.find_repeated_letters(sample_string_2))