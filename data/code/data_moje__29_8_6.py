import re

class VowelCounter:
    VOWEL_PATTERN = re.compile(r'[aeiouAEIOU]')

    @staticmethod
    def count_vowels(text):
        matches = VowelCounter.VOWEL_PATTERN.findall(text)
        return len(matches)

if __name__ == '__main__':
    test_string = "Python programming is fun!"
    result = VowelCounter.count_vowels(test_string)
    print(result)