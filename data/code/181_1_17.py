import re

def find_vowels(text):
    vowels = set()
    pattern = re.compile(r'[aeiou]', re.IGNORECASE)
    for match in pattern.finditer(text):
        vowels.add(match.group().lower())
    return vowels

if __name__ == '__main__':
    sample1 = "Example text with vowels"
    sample2 = "Vowels: AEIOUaeiou"
    sample3 = "Sample string without vowels"
    sample4 = "Python programming is awesome"
    
    result1 = find_vowels(sample1)
    result2 = find_vowels(sample2)
    result3 = find_vowels(sample3)
    result4 = find_vowels(sample4)

    print(f"Vowels in '{sample1}': {result1}")
    print(f"Vowels in '{sample2}': {result2}")
    print(f"Vowels in '{sample3}': {result3}")
    print(f"Vowels in '{sample4}': {result4}")