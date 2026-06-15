def find_vowels(text):
    vowels = set()
    for char in text:
        if 'a' <= char.lower() <= 'z':
            if char.lower() in 'aeiou':
                vowels.add(char.lower())
    return vowels
if __name__ == '__main__':
    test_string1 = "Hello World"
    result1 = find_vowels(test_string1)
    print(f"Vowels in '{test_string1}': {result1}")
    test_string2 = "AEIOUaeiou"
    result2 = find_vowels(test_string2)
    print(f"Vowels in '{test_string2}': {result2}")
    test_string3 = "Rhythm"
    result3 = find_vowels(test_string3)
    print(f"Vowels in '{test_string3}': {result3}")
    test_string4 = "Programming is Fun"
    result4 = find_vowels(test_string4)
    print(f"Vowels in '{test_string4}': {result4}")