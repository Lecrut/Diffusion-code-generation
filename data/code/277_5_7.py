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
    sample_text = "Hello World"
    non_vowel_count = counter.count_non_vowels(sample_text)
    print(f"Number of non-vowel characters in '{sample_text}': {non_vowel_count}")