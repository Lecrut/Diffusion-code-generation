class VowelIdentifier:
    def extract_vowels(self, text):
        vowels = "aeiouAEIOU"
        extracted_vowels = []
        for char in text:
            if char in vowels:
                extracted_vowels.append(char)
        return extracted_vowels
if __name__ == '__main__':
    identifier = VowelIdentifier()
    sample_text1 = "Hello World"
    sample_text2 = "Programming is fun"
    sample_text3 = "AEIOUaeiou 123"
    result1 = identifier.extract_vowels(sample_text1)
    print(f"Text: '{sample_text1}'")
    print(f"Vowels: {result1}")
    result2 = identifier.extract_vowels(sample_text2)
    print(f"Text: '{sample_text2}'")
    print(f"Vowels: {result2}")
    result3 = identifier.extract_vowels(sample_text3)
    print(f"Text: '{sample_text3}'")
    print(f"Vowels: {result3}")