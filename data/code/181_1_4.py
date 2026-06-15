def find_vowels(text):
    vowels = set()
    for char in text:
        if 'a' <= char.lower() <= 'z':
            if char.lower() in 'aeiou':
                vowels.add(char.lower())
    return vowels
if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "AEIOUaeiou"
    sample3 = "Rhythm"
    sample4 = "Programming is Fun"
    result1 = find_vowels(sample1)
    result2 = find_vowels(sample2)
    result3 = find_vowels(sample3)
    result4 = find_vowels(sample4)
    print(f"Vowels in '{sample1}': {result1}")
    print(f"Vowels in '{sample2}': {result2}")
    print(f"Vowels in '{sample3}': {result3}")
    print(f"Vowels in '{sample4}': {result4}")