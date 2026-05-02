class StringProcessor:
    def count_vowels(self, text):
        count = 0
        vowels = "aeiouAEIOU"
        for char in text:
            if char in vowels:
                count += 1
        return count
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string1 = "Hello World"
    sample_string2 = "Programming is Fun"
    sample_string3 = "AEIOUaeiou"
    sample_string4 = "Rhythm"
    result1 = processor.count_vowels(sample_string1)
    result2 = processor.count_vowels(sample_string2)
    result3 = processor.count_vowels(sample_string3)
    result4 = processor.count_vowels(sample_string4)
    print(f"'{sample_string1}': {result1}")
    print(f"'{sample_string2}': {result2}")
    print(f"'{sample_string3}': {result3}")
    print(f"'{sample_string4}': {result4}")