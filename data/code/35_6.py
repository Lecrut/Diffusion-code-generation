class StringProcessor:
    def count_vowels(self, text: str) -> int:
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
    sample_string3 = "AEIOUaeiou123"
    sample_string4 = "Rhythm"
    result1 = processor.count_vowels(sample_string1)
    result2 = processor.count_vowels(sample_string2)
    result3 = processor.count_vowels(sample_string3)
    result4 = processor.count_vowels(sample_string4)
    print(f"'{sample_string1}' has {result1} vowels")
    print(f"'{sample_string2}' has {result2} vowels")
    print(f"'{sample_string3}' has {result3} vowels")
    print(f"'{sample_string4}' has {result4} vowels")