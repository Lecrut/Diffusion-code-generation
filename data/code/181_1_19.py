import re

class VowelFinder:
    def __init__(self):
        self.vowels = set('aeiou')

    def find_vowels(self, text):
        return list(set(re.findall(r'[aeiou]', text.lower())))

if __name__ == '__main__':
    finder = VowelFinder()
    sample1 = "Hello World"
    sample2 = "AEIOUaeiou123"
    sample3 = "Rhythm"
    sample4 = "Programming is Fun"

    print(f"Vowels in '{sample1}': {finder.find_vowels(sample1)}")
    print(f"Vowels in '{sample2}': {finder.find_vowels(sample2)}")
    print(f"Vowels in '{sample3}': {finder.find_vowels(sample3)}")
    print(f"Vowels in '{sample4}': {finder.find_vowels(sample4)}")