import re

class StringNormalizer:
    def normalize(self, text):
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return [word.lower() for word in cleaned_text.split()]

if __name__ == '__main__':
    normalizer = StringNormalizer()
    sample_string = "This is a long!@# sentence with special characters & symbols."
    normalized_words = normalizer.normalize(sample_string)
    print(normalized_words)