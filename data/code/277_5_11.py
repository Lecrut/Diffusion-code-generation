class CharacterCounter:
    def count_non_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char not in vowels:
                count += 1
        return count

if __name__ == '__main__':
    counter = CharacterCounter()
    sample_text1 = "Hello, World!"
    non_vowel_count1 = counter.count_non_vowels(sample_text1)
    print(f"Non-vowel characters in '{sample_text1}': {non_vowel_count1}")

    sample_text2 = "Python Programming"
    non_vowel_count2 = counter.count_non_vowels(sample_text2)
    print(f"Non-vowel characters in '{sample_text2}': {non_vowel_count2}")