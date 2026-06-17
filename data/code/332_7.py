class TextProcessor:
    def count_vowels(self, text: str) -> int:
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        return count
if __name__ == '__main__':
    processor = TextProcessor()
    sample_string_one = "Hello World"
    sample_string_two = "Programming is fun"
    sample_string_three = "AEIOUaeiou"
    count_one = processor.count_vowels(sample_string_one)
    print(f"Vowel count for '{sample_string_one}': {count_one}")
    count_two = processor.count_vowels(sample_string_two)
    print(f"Vowel count for '{sample_string_two}': {count_two}")
    count_three = processor.count_vowels(sample_string_three)
    print(f"Vowel count for '{sample_string_three}': {count_three}")