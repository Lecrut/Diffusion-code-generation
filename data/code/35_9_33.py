class VowelCounter:
    VOWELS = set("aeiouAEIOU")

    @staticmethod
    def count_vowels(text: str) -> int:
        return sum(1 for char in text if char in VowelCounter.VOWELS)

if __name__ == '__main__':
    sample_string_1 = "Hello World"
    sample_string_2 = "Programming is Fun"
    sample_string_3 = "AEIOUaeiou"
    sample_string_4 = "Rhythm"
    
    count1 = VowelCounter.count_vowels(sample_string_1)
    count2 = VowelCounter.count_vowels(sample_string_2)
    count3 = VowelCounter.count_vowels(sample_string_3)
    count4 = VowelCounter.count_vowels(sample_string_4)
    
    print(f"'{sample_string_1}': {count1}")
    print(f"'{sample_string_2}': {count2}")
    print(f"'{sample_string_3}': {count3}")
    print(f"'{sample_string_4}': {count4}")