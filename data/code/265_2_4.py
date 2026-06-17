class StringExtractor:
    def extract_specific_chars(self, text, char_set):
        extracted_chars = ""
        for char in text:
            if char in char_set:
                extracted_chars += char
        return extracted_chars
if __name__ == '__main__':
    extractor = StringExtractor()
    sample_text = "Hello World! 123"
    allowed_chars_set = set("aeiouAEIOU0123456789")
    result = extractor.extract_specific_chars(sample_text, allowed_chars_set)
    print(result)