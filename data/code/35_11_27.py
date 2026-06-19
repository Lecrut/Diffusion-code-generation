class VowelCounter:
    VOWELS = "aeiouAEIOU"

    @staticmethod
    def count_vowels(text):
        return sum(1 for char in text if char in VowelCounter.VOWELS)

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Python Programming"
    sample_string_3 = "Rhythm"
    sample_string_4 = "AEIOUaeiou123!"
    print(f"'{sample_string_1}': {VowelCounter.count_vowels(sample_string_1)}")
    print(f"'{sample_string_2}': {VowelCounter.count_vowels(sample_string_2)}")
    print(f"'{sample_string_3}': {VowelCounter.count_vowels(sample_string_3)}")
    print(f"'{sample_string_4}': {VowelCounter.count_vowels(sample_string_4)}")