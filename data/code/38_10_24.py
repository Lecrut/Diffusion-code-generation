class LetterFinder:
    ALPHABET = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @staticmethod
    def find_repeated_letters(input_string):
        seen_letters = set()
        repeated_letters = set()
        for char in input_string:
            if char in LetterFinder.ALPHABET:
                if char.lower() in seen_letters:
                    repeated_letters.add(char.lower())
                else:
                    seen_letters.add(char.lower())
        return repeated_letters

if __name__ == '__main__':
    sample_string_1 = "Hello, World!"
    result_1 = LetterFinder.find_repeated_letters(sample_string_1)
    print("Repeated letters in", sample_string_1, ":", result_1)

    sample_string_2 = "Alphabet and numbers 123"
    result_2 = LetterFinder.find_repeated_letters(sample_string_2)
    print("Repeated letters in", sample_string_2, ":", result_2)

    sample_string_3 = "Python programming"
    result_3 = LetterFinder.find_repeated_letters(sample_string_3)
    print("Repeated letters in", sample_string_3, ":", result_3)