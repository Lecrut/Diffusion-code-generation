class VowelCounter:
    VOWELS = set('aeiouAEIOU')

    @staticmethod
    def count_non_vowels(input_string):
        non_vowel_count = 0
        for char in input_string:
            if char not in VowelCounter.VOWELS:
                non_vowel_count += 1
        return non_vowel_count

if __name__ == '__main__':
    counter = VowelCounter()
    sample_string = "Hello, World!"
    result = counter.count_non_vowels(sample_string)
    print(f"Number of non-vowel characters in '{sample_string}': {result}")