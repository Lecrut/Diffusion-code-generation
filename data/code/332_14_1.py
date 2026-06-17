class TextProcessor:
    @staticmethod
    def count_vowels(word):
        vowels = "aeiouAEIOU"
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count
if __name__ == '__main__':
    test_word_1 = "Hello World"
    result_1 = TextProcessor.count_vowels(test_word_1)
    print(f"Vowel count in '{test_word_1}': {result_1}")
    test_word_2 = "Programming"
    result_2 = TextProcessor.count_vowels(test_word_2)
    print(f"Vowel count in '{test_word_2}': {result_2}")
    test_word_3 = "Rhythm"
    result_3 = TextProcessor.count_vowels(test_word_3)
    print(f"Vowel count in '{test_word_3}': {result_3}")