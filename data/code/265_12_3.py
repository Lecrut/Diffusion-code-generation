class StringExtractor:
    def extract(self, text):
        vowels = "aeiou"
        extracted_vowels = ""
        for char in text:
            if char.lower() in vowels:
                extracted_vowels += char.lower()
        return extracted_vowels
if __name__ == '__main__':
    extractor = StringExtractor()
    sample_text1 = "This is a sample text for vowel extraction"
    sample_text2 = "Rhythm myth sky"
    sample_text3 = "AEIOUaeiou 123"
    result1 = extractor.extract(sample_text1)
    result2 = extractor.extract(sample_text2)
    result3 = extractor.extract(sample_text3)
    print(f"Text: '{sample_text1}'")
    print(f"Extracted Vowels: '{result1}'")
    print("-" * 20)
    print(f"Text: '{sample_text2}'")
    print(f"Extracted Vowels: '{result2}'")
    print("-" * 20)
    print(f"Text: '{sample_text3}'")
    print(f"Extracted Vowels: '{result3}'")