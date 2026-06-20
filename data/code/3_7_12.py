class TextProcessor:
    VOWELS = frozenset("aeiouAEIOU")

    @staticmethod
    def remove_vowels(text):
        return "".join([char for char in text if char not in TextProcessor.VOWELS])

if __name__ == "__main__":
    processor = TextProcessor()
    sample_text = "The quick brown fox jumps over the lazy dog"
    cleaned_text = processor.remove_vowels(sample_text)
    print(cleaned_text)