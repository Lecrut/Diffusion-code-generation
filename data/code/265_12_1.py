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
    sample_text1 = "Hello World"
    sample_text2 = "Programming is Fun"
    sample_text3 = "AEIOUaeiou 123"
    result1 = extractor.extract(sample_text1)
    result2 = extractor.extract(sample_text2)
    result3 = extractor.extract(sample_text3)
    print(f"'{sample_text1}' -> '{result1}'")
    print(f"'{sample_text2}' -> '{result2}'")
    print(f"'{sample_text3}' -> '{result3}'")