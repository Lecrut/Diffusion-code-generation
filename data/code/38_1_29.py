class LetterFrequencyAnalyzer:
    LOWERCASE_A = ord('a')
    LOWERCASE_Z = ord('z')

    @staticmethod
    def is_lowercase_letter(char):
        return LetterFrequencyAnalyzer.LOWERCASE_A <= ord(char) <= LetterFrequencyAnalyzer.LOWERCASE_Z

    @staticmethod
    def find_repeated_letters(s):
        letter_counts = {}
        for char in s:
            if LetterFrequencyAnalyzer.is_lowercase_letter(char):
                letter_counts[char] = letter_counts.get(char, 0) + 1
        repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
        return repeated_letters

if __name__ == '__main__':
    test_string_1 = "hello world"
    result_1 = LetterFrequencyAnalyzer.find_repeated_letters(test_string_1)
    print(f"Input: '{test_string_1}', Repeated Letters: {result_1}")
    
    test_string_2 = "programming"
    result_2 = LetterFrequencyAnalyzer.find_repeated_letters(test_string_2)
    print(f"Input: '{test_string_2}', Repeated Letters: {result_2}")
    
    test_string_3 = "abcde"
    result_3 = LetterFrequencyAnalyzer.find_repeated_letters(test_string_3)
    print(f"Input: '{test_string_3}', Repeated Letters: {result_3}")