class VowelCounter:
    def __init__(self, word):
        self.word = word
    def get_vowel_count(self):
        vowels = "aeiouAEIOU"
        count = 0
        for char in self.word:
            if char in vowels:
                count += 1
        return count
if __name__ == '__main__':
    sample_word = "programming"
    counter = VowelCounter(sample_word)
    vowel_count = counter.get_vowel_count()
    print(f"The word is: {sample_word}")
    print(f"The vowel count is: {vowel_count}")
    sample_word_2 = "AEIOUaeiou"
    counter_2 = VowelCounter(sample_word_2)
    vowel_count_2 = counter_2.get_vowel_count()
    print(f"The word is: {sample_word_2}")
    print(f"The vowel count is: {vowel_count_2}")