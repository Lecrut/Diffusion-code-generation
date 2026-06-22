class CharacterCounter:
    def count_non_vowels(self, input_string):
        vowels = "aeiouAEIOU"
        count = 0
        for char in input_string:
            if char not in vowels:
                count += 1
        return count

if __name__ == '__main__':
    counter = CharacterCounter()
    sample_string = "Hello, World!"
    non_vowel_count = counter.count_non_vowels(sample_string)
    print(f"Number of non-vowel characters in '{sample_string}': {non_vowel_count}")