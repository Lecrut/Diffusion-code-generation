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
    sample_word = "Programming"
    counter = VowelCounter(sample_word)
    vowel_count = counter.get_vowel_count()
    print(vowel_count)