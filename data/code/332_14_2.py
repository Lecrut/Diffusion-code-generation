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
    word1 = "Hello World"
    word2 = "Python Programming"
    word3 = "Rhythm"
    print(f"Vowel count in '{word1}': {TextProcessor.count_vowels(word1)}")
    print(f"Vowel count in '{word2}': {TextProcessor.count_vowels(word2)}")
    print(f"Vowel count in '{word3}': {TextProcessor.count_vowels(word3)}")