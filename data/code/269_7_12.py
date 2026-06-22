import string

class PunctuationCleaner:
    PUNCTUATION_CHARS = set(string.punctuation)

    @staticmethod
    def remove_duplicates(text):
        seen = set()
        result = []
        for char in text:
            if char in PunctuationCleaner.PUNCTUATION_CHARS and char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with punctuation."
    cleaner = PunctuationCleaner()
    cleaned_string = cleaner.remove_duplicates(sample_string)
    print(cleaned_string)