import re

VOWEL_PATTERN = r'[aeiouAEIOU]'

class VowelCounter:
    @staticmethod
    def count(text):
        matches = re.findall(VowelCounter.get_pattern(), text)
        return len(matches)

    @staticmethod
    def get_pattern():
        return VOWEL_PATTERN

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    count = VowelCounter.count(sample_text)
    print(count)