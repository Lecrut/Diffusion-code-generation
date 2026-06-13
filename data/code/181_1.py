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
    print(f"Vowels in '{sample1}': {find_vowels(sample1)}")
    print(f"Vowels in '{sample2}': {find_vowels(sample2)}")
    print(f"Vowels in '{sample3}': {find_vowels(sample3)}")
    print(f"Vowels in '{sample4}': {find_vowels(sample4)}")