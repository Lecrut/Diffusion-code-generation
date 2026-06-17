class StringProcessor:
    def find_punctuation(self, text):
        punctuation = []
        for char in text:
            if not char.isalnum():
                punctuation.append(char)
        return punctuation
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string1 = "Hello, world! This is a test string."
    sample_string2 = "Python3.10 is great!"
    sample_string3 = "NoPunctuationHere"
    sample_string4 = "!@#$%^&*()_+=-`~"
    result1 = processor.find_punctuation(sample_string1)
    print(f"String: '{sample_string1}'")
    print(f"Punctuation: {result1}")
    result2 = processor.find_punctuation(sample_string2)
    print(f"String: '{sample_string2}'")
    print(f"Punctuation: {result2}")
    result3 = processor.find_punctuation(sample_string3)
    print(f"String: '{sample_string3}'")
    print(f"Punctuation: {result3}")
    result4 = processor.find_punctuation(sample_string4)
    print(f"String: '{sample_string4}'")
    print(f"Punctuation: {result4}")