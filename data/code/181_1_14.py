import re

class VowelFinder:
    def __init__(self):
        self.vowels = set('aeiou')

    def find_vowels_in_text(self, text):
        return set(match for match in re.findall(r'[aeiou]', text.lower()))

if __name__ == '__main__':
    finder = VowelFinder()
    sample1 = "Hello World"
    sample2 = "AEIOUaeiou"
    sample3 = "Rhythm"
    sample4 = "Programming is Fun"

    result1 = finder.find_vowels_in_text(sample1)
    result2 = finder.find_vowels_in_text(sample2)
    result3 = finder.find_vowels_in_text(sample3)
    result4 = finder.find_vowels_in_text(sample4)

    print(f"Vowels in '{sample1}': {result1}")
    print(f"Vowels in '{sample2}': {result2}")
    print(f"Vowels in '{sample3}': {result3}")
    print(f"Vowels in '{sample4}': {result4}")